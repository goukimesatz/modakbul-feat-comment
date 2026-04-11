# 유저 생성, 조회 쿼리

from schemas.auth import UserCreate
from db.connection import get_db_connection
import core.security

def create_user(user_data: UserCreate) -> dict:
    """
    TODO: [?] 회원가입 DB INSERT 로직
    1. core.security.get_password_hash()로 비밀번호 암호화
    2. with get_db_connection as conn: 열고 INSERT 쿼리 날리기
    3. 만약 이미 있는 아이디면 예외 발생시키기 (라우터가 409 에러를 잡을 수 있도록)
    """
    pass

def authenticate_user(username: str, password: str) -> dict:
    """
    TODO: [?] 로그인 DB 검증 로직
    1. SELECT * FROM user WHERE username = ? 로 유저 찾기
    2. core.security.verify_password()로 비밀번호가 맞는지 확인
    3. 성공하면 유저 딕셔너리 반환, 실패하면 None 반환
    """
    pass