from typing import Dict
from uuid import UUID

users_db: Dict[UUID, dict] = {}
topics_db: Dict[UUID, dict] = {}
comments_db: Dict[UUID, dict] = {}

def get_db():
    return {
        "users": users_db,
        "topics": topics_db,
        "comments": comments_db
    }
