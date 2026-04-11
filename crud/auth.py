# 유저 생성, 조회 쿼리

import sqlite3
from schemas.auth import UserCreate
from db.connection import get_db_connection
from core.exceptions import UserAlreadyExistsException
import core.security

def create_user(user_data: UserCreate) -> dict:
    """ 새로운 사용자를 DB에 생성합니다.

    입력받은 평문 비밀번호는 내부적으로 단방향 해싱(bcrypt) 처리되어 저장됩니다.

    Args:
        user_data (UserCreate): 가입할 사용자의 정보(username, password, nickname)가 담긴 스키마
         
    Returns:
        dict: 생성된 사용자의 정보 (password_hash는 제외)

    Raises:
        UserAlreadyExistsException: 입력한 username(ID)이 이미 DB에 존재할 경우 발생
    """

    """
    TODO: [?] 회원가입 DB INSERT 로직
    1. core.security.get_password_hash()로 비밀번호 암호화
    2. with get_db_connection as conn: 열고 INSERT 쿼리 날리기
    3. 만약 sqlite3.IntegrityError가 터지면 UserAlreadyExistsException() 던지기
    """
    pass

def authenticate_user(username: str, password: str) -> dict:
    """ 사용자의 로그인 자격 증명을 검증합니다.

    DB에 해당 ID가 존재하는지 먼저 확인하고,
    입력된 평문 비밀번호와 DB의 해시된 비밀번호가 일치하는지 검증합니다.

    Args:
        username (str): 로그인 시도하는 사용자의 ID
        password (str): 로그인 시도하는 사용자의 평문 비밀번호
    
    Returns:
        dict: 인증에 성공한 사용자의 DB 레코드 정보

    Raises:
        InvalidCredentialsException: 아이디가 존재하지 않거나, 비밀번호가 틀릴 경우 발생

    """
   
    """
    TODO: [?] 로그인 DB 검증 로직
    1. SELECT * FROM user WHERE username = ? 로 유저 찾기
    2. 유저가 없거나, core.security.verify_password() 결과가 False라면
        InvalidCredentialsException() 던지기
    3. 성공하면 유저 딕셔너리 반환
    """
    pass