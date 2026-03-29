from fastapi import FastAPI, HTTPException, status, Depends
from uuid import UUID, uuid4

# for password hasing
import bcrypt
from starlette.status import HTTP_201_CREATED

# my created
import schemas
from store import get_db

# for topic TTL and uniqueness
from datetime import datetime, timedelta, timezone
import hashlib

app = FastAPI(
    title="Campfire API",
    description="Ephemeral discussion API",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "The campfire is lit."}

# USER ENDPOINT
@app.post("/users/register", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(
    user: schemas.UserCreate,
    db: dict = Depends(get_db)
):
    for existing_user in db["users"].values():
        if existing_user["username"] == user.username:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User Name already taken")

    salt = bcrypt.gensalt()
    hashed_pw = bcrypt.hashpw(user.password.encode('utf-8'), salt)

    new_user_id = uuid4()
    new_user = {
        "id": new_user_id,
        "username": user.username,
        "password": hashed_pw
    }

    db["users"][new_user_id] = new_user

    return new_user

@app.post("/users/login")
def login_user(
    user: schemas.UserCreate,
    db: dict = Depends(get_db)
):
    target_user = None
    for existing_user in db["users"].values():
        if existing_user["username"] == user.username:
            target_user = existing_user
            break

    if not target_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")

    if not bcrypt.checkpw(user.password.encode('utf-8'), target_user["password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")

    return {"message": "Login successfull", "user_id": target_user["id"]}

@app.post("/topics", response_model=schemas.TopicResponse, status_code=HTTP_201_CREATED)
def create_topic(
    topic: schemas.TopicCreate,
    owner_id: str,
    db: dict = Depends(get_db)
):
    try:
        user_uuid = UUID(owner_id)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid UUID fromat")

    if user_uuid not in db["users"]:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    content_hash = hashlib.sha256(topic.content.encode('utf-8')).hexdigest()

    for existing_topic in db["topics"].values():
        if existing_topic["topic_hash"] == content_hash:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="A topic with this exact content already exists")

    new_topic_id = uuid4()
    creation_time = datetime.now(timezone.utc)
    initial_ttl = creation_time + timedelta(hours=1)

    new_topic = {
        "id": new_topic_id,
        "owner_id": user_uuid,
        "content": topic.content,
        "topic_hash": content_hash,
        "ttl": initial_ttl,
        "current_comment_number": 0,
        "previous_comment_number": 0,
        "total_comment_number": 0
    }

    db["topics"][new_topic_id] = new_topic

    return new_topic

@app.get("/topic", response_model=list[schemas.TopicResponse])
def get_active_topics(db: dict = Depends(get_db)):
    # For now, return all the topics
    # TODO: Later filter the expired topics
    return list(db["topics"].values())
