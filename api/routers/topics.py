# GET /topics, POST /topics 등

from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from schemas.topics import TopicCreate, TopicResponse
from api.dependencies import get_current_user
import crud.topics

router = APIRouter(prefix="/topics", tags=["Topics"])

@router.post("/", response_model=TopicResponse, status_code=201)
def create_new_topic(
    topic_data: TopicCreate,
    user_id: int = Depends(get_current_user)
):
    """
    새로운 모닥불을 피웁니다. (로그인 필수)
    """
    # TODO: [?] crud.topics.create_topic(topic_data, user_id) 호출 후 결과 반환
    pass


@router.get("/", response_model=List[TopicResponse])
def read_topic_feed(
    limit: int = Query(20, ge=1, le=100, description="가져올 게시물 수"),
    offset: int = Query(0, ge=0, description="건너뛸 게시물 수")
):
    """
    현재 살아있는 모닥불 피드를 조회합니다. (페이징 지원)
    """
    # TODO: [?] crud.topics.get_active_topics(limit, offset) 호출 후 리턴
    return []


@router.get("/{topic_id}", response_model=TopicResponse)
def get_topic_detail(topic_id: int):
    """
    특정 모닥불의 상세 내용을 조회합니다.
    """
    # TODO: [?] crud.topics.get_topic_detail(topic_id) 호출
    # 만료되었거나 없는 게시물이면 HTTPException(status_code=404) 발생
    pass