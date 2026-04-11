# 토큰 검증, 로그인 유저 식별 등 공통 함수 (Depends)

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

# Set Basic URL
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)) -> int:
    """
    TODO: [?] JWT 토큰을 해독하고 검증하여 user_id를 반환하는 로직 작성
    - 토큰 만료 시 401 Unauthorized 반환
    - 조작된 토큰일 시 401 Unauthorized 반환
    """
    
    # temporary dummy data (development)
    dummy_user_id = 1
    return dummy_user_id