# 장작 추가 및 가변 연소율 시간 계산 로직

from schemas.comments import CommentCreate
from core.exceptions import TopicNotFoundException, TopicAlreadyExpiredException
from db.connection import get_db_connection

def create_comment(topic_id: int, comment_data: CommentCreate, user_id: int) -> dict:
    """ 살아있는 모닥불에 새로운 장작(Comment)을 추가하고 수명을 연장합니다.

    단일 트랜잭션을 사용하여 댓글 추가와 가변 연소율 기반의 수명 연장을 동시에 처리합니다.

    Args:
        topic_id (int) : 장작을 넣을 대상 모닥불의 고유 ID
        comment_data (CommentCreate): 추가할 장작의 내용이 담긴 스키마
        user_id (int) 장작을 넣는 사용자의 고유 ID
    Returns:
        dict: DB에 방금 삽입된 장작(댓글)의 상세 정보 딕셔너리

    Raises:
        TopicNotFoundException: 해당 ID의 모닥불의 DB에 존재하지 않을 경우 발생
        TopicAlreadyExpiredException: 모닥불이 이미 수명을 다하여 꺼진 경우 발생
    """
    
    
    """
    TODO: [?] SYS-07 장작 추가 및 가변 연소율 시간 연장 (트랜잭션 필수)
    
    with get_db_connection() as conn:
        cursor = conn.cursor()
        # 1. 모닥불이 살아있는지, 현재 장작(comment_count)이 몇 개인지 SELECT
        # 2. if/elif 문으로 가변 연소율 시간 게산 (0~9: 10분, 10~49: 5분, ...)

        try:
            # 3. 장작 데이터 INSERT (comments) 테이블
            # 4. 모닥불 생명 연장 UPDATE (topics 테이블의 expires_at, comment_count + 1)
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        # 5. 방금 달린 댓글 정보 반환
    """
    pass
