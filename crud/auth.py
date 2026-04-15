# 유저 생성, 조회 쿼리

import sqlite3
from schemas.auth import UserCreate
from db.connection import get_db_connection
from core.exceptions import UserAlreadyExistsException, InvalidCredentialsException
from core.security import get_password_hash, verify_password

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
    
    # 1. 비밀번호 해싱
    hashed_password = get_password_hash(user_data.password)

    # 2. DB Connection 열어서 쿼리를 실행하기
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()

            # INSERT 쿼리
            # SQL Injection 방지를 위하여 '?' placeholder 사용
            query = "INSERT INTO users (username, password_hash, nickname) VALUES (?, ?, ?)"
            cursor.execute(query, (user_data.username, hashed_password, user_data.nickname))

            # 변경사항 저장
            conn.commit()

            # INSERT된 데이터의 고유 ID(Primary Key) 가져오기
            new_user_id = cursor.lastrowid

    except sqlite3.IntegrityError:
        # 3. username의 UNIQUE constraint 위배할 경우 발생 (username 중복)
        raise UserAlreadyExistsException()
    
    return {
        "id": new_user_id,
        "username": user_data.username,
        "nickname": user_data.nickname
    }
    


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
   
    # 1. DB Connection 열어서 유저 찾기
    with get_db_connection() as conn:
        cursor = conn.cursor()

        # id, username, nickname, password_hash를 가져오기
        query = "SELECT id, username, nickname, password_hash FROM users WHERE username = ?"
        cursor.execute(query, (username, ))
        user_record = cursor.fetchone()

    # 2-1. 유저가 DB에 없는 경우
    if user_record is None:
        raise InvalidCredentialsException()
    
    # 가져온 record(tuple) unpacking
    user_id, db_username, db_nickname, db_password_hash = user_record

    # 2-2. 비밀번호 검증
    # verify_password가 False를 반환하면(비밀번호가 틀리면) 에러 던지기
    if not verify_password(password, db_password_hash):
        raise InvalidCredentialsException()
    
    # 3. 인증을 모두 무사히 통과하여 유저 정보 딕셔너리 반환
    return {
        "id": user_id,
        "username": db_username,
        "nickname": db_nickname
    }
