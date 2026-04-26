# FastAPI 앱 실행의 진입점

from fastapi import FastAPI
from contextlib import asynccontextmanager
from db.init_db import init_db
from api.routers import auth, topics, comments

# Lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):

    # 1. Initialize DB file & Table
    init_db()

    # TODO: Add Scheduler start logics.

    yield

    # Logic when server shutdown.

app = FastAPI(
    title="Modakbul API",
    description="시간이 지나면 꺼지는 휘발성 모닥불 커뮤니티",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(auth.router, prefix="/api")
app.include_router(topics.router, prefix="/api")
app.include_router(comments.router, prefix="/api")

@app.get("/")
def root():
    return {
        "message" : "모닥불(Modakbul) 서버가 활활 타오르고 있습니다."
    }