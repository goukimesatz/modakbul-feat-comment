# 모닥불 생성, 지연 삭제 필터링 조회가 포함된 쿼리

from typing import List, Optional
from schemas.topics import TopicCreate, TopicResponse
from db.connection import get_db_connection
from datetime import datetime, timedelta

def create_topic(topic_data: TopicCreate, user_id: int) -> dict:
    """
    TODO: [?] 모닥불 피우기
    1. INSERT INTO topics 로 데이터 삽입
    2. 삽입할 때 expires_at 값을 '현재 시간 + 1시간'으로 계산하여 넣기
    3. 방금 생성된 데이터(id 포함)를 SELECT 해서 리턴하기
    """
    pass

def get_active_topics(limit: int = 20, offset: int = 0) -> List[dict]:
    """
    TODO: [?] SYS-05 지연 삭제가 적용된 피드 목록
    1. SELECT * FROM topics WHERE expires_at > datetime('now') ORDER BY expires_at DESC LIMIT ? OFFSET ?
    2. 결과를 리스트로 묶어서 리턴
    """
    return []

def get_topic_detail(topic_id: int) -> Optional[dict]:
    """
    TODO: [?] 모닥불 상세 조회
    1. SELECT * FROM topics WHERE id = ?
    2. 만약 가져온 데이터의 expires_at이 과거라면 None 반환 (라우터가 404 처리)
    """
    pass