# 장작 추가 및 가변 연소율 시간 계산 로직

from schemas.comments import CommentCreate
from db.connection import get_db_connection

def create_comment(topic_id: int, comment_data: CommentCreate, user_id: int) -> dict:
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
