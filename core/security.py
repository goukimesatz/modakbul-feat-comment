# bcrypt 해싱 함수, JWT 생성 함수 등

from datetime import datetime, timedelta

def get_password_hash(password: str) -> str:
    """평문 비밀번호를 단방향 암호화(해싱)하여 반환합니다.

    보안을 위해 bcrypt 알고리즘을 적용하여 솔트(Salt)가 포함된 해시값을 생성합니다.
    
    Args:
        password (str): 사용자가 입력한 평문 비밀번호

    Returns:
        str: DB에 안전하게 저장할 수 있는 해싱된 비밀번호 문자열

    """

    """
    TODO: [?] passlib을 이용해 평문 비밀번호를 bcrypt로 해싱하여 반환
    """
    return "dummy_hashed_password"

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """로그인 시 입력받은 평문 비밀번호가 DB의 해시와 일치하는지 검증합니다.

    Args:
        plain_password (str): 사용자가 로그인 폼에 입력한 평문 비밀번호
        hashed_password (str): DB에 저장되어 있던 해시된 비밀번호

    Returns:
        bool: 두 비밀번호가 일치하면 True, 틀리면 False
    
    """
    
    """
    TODO: [?] 로그인 시 입력받은 평문과 DB의 해시가 일치하는지 검증
    """
    return True

def create_access_token(data: dict) -> str:
    """사용자 식별 데이터를 담은 JWT(JSON Web Token) 액세스 토큰을 생성합니다.

    보안을 위해 전달받은 페이로드(data)에 토큰 만료 시간(exp)을 자동으로 추가한 뒤 서명하여 반환합니다.

    Args:
        data (dict): 토큰 페이로드에 담을 데이터 (예: {"sub": "user_id"})

    Returns:
        str: 헤더(Header), 페이로드(Payload), 서명(Signature)이 포함된 JWT 문자열
    
    """

    """
    TODO: [?] PyJWT을 이용해 access_token 생성 후 반환 (만료시간 포함)
    1. data 딕셔너리를 깊은 복사(deep copy)하여 원본 훼손 방지
    2. 복사한 딕셔너리에 'exp' (현재시간 + 만료시간) 키 추가
    3. jwt.encode()를 사용하여 토큰 생성 후 리턴
    """
    return "dummy_jwt_token"