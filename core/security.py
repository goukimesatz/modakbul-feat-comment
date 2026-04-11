# bcrypt 해싱 함수, JWT 생성 함수 등

def get_password_hash(password: str) -> str:
    """
    TODO: [?] passlib을 이용해 평문 비밀번호를 bcrypt로 해싱하여 반환
    """
    return "dummy_hashed_password"

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    TODO: [?] 로그인 시 입력받은 평문과 DB의 해시가 일치하는지 검증
    """
    return True

def create_access_token(data: dict) -> str:
    """
    TODO: [?] PyJWT을 이용해 access_token 생성 후 반환 (만료시간 포함)
    """
    return "dummy_jwt_token"