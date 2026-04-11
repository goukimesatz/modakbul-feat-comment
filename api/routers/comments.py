# POST /topics/{id}/comments 등

from fastapi import APIRouter, Depends, HTTPException
from schemas.comments import CommentCreate, CommentResponse
from api.dependencies import get_current_user
import crud.comments

router = APIRouter(prefix="/comments", tags=["Comments"])

@router.post(
        "/{topic_id}/comments",
        response_model=CommentResponse,
        status_code=201)
def add_comment_to_topic(
    topic_id: int,
    comment_data: CommentCreate,
    user_id: int = Depends(get_current_user)
):
    """
    살아있는 모닥불에 장작(댓글)을 추가하여 수명을 연장합니다. (로그인 필수)
    """
    # TODO: [?] crud.comments.create_comment(topic_id, comment_data, user_id) 호출
    # 모닥불이 이미 만료되었거나 존재하지 않으면 HTTPException(status_code=404) 발생
    # (주의) 시간 연장 로직은 여기서 짜지 말고 crud/comments.py 내부 쿼리에 맡길 것.