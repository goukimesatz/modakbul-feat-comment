# POST /auth/signup, /auth/login 등

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from schemas.auth import UserCreate, TokenResponse
import crud.auth

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post(
    "/signup",
    response_model=dict,
    status_code=status.HTTP_201_CREATED)
def signup(user_data: UserCreate):
    """
    새로운 이용자를 생성합니다.
    """
    # TODO: [?] crud.auth.create_user(user_data) 호출
    # 이미 존재하는 아이디일 경우 HTTPException(status_code=409) 발생
    return {
        "message" : "회원가입이 완료되었습니다."
    }

@router.post("/login", response_model=TokenResponse)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    로그인하여 JWT 토큰을 발급받습니다.
    """
    # TODO: [?] crud.auth.authenticate_user(form_data.username, form_data.password) 호출
    # 인증 실패 시 HTTPException(status_code=401) 발생
    # core.security.create_access_token() 호출하여 토큰 생성

    return {
        "access_token": "dummy_jwt_token",
        "token_type" : "bearer"
    }

@router.post("/logout")
def logout():
    """
    로그아웃 처리를 수행합니다.
    """
    # TODO: [?] 클라이언트 측에서 토큰을 지우도록 유도하거나, 블랙리스트 처리 로직 구현
    return {
        "message" : "로그아웃 되었습니다."
    }