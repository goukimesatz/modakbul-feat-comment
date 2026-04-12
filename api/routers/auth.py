# POST /auth/signup, /auth/login 등

from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from schemas.auth import UserCreate, TokenResponse
import crud.auth
import core.security

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post(
    "/signup",
    response_model=dict,
    status_code=status.HTTP_201_CREATED,
    summary="회원가입",
    description="새로운 사용자를 생성합니다."
    )
def signup(user_data: UserCreate):
    """새로운 사용자를 DB에 등록합니다.

    Args:
        user_data (UserCreate): 클라이언트가 전달한 회원가입 정보(username, password, nickname)

    Returns:
        dict: 회원가입 성공 메시지
    
    Raises:
        UserAlreadyExistsException: (CRUD 내부에서 발생) 이미 존재하는 아이디일 경우 409 반환
    """
    """
    TODO: [?] 회원가입 처리 로직
    1. crud.auth.create_user(user_date) 호출
    2. (참고: 중복 아이디 에러는 CRUD 쪽에서 알아서 던지고 전역 핸들러가 처리하므로, 라우터에서는 try-exception 없이 호출만 하면 됨.)
    """
    return {
        "message" : "회원가입이 완료되었습니다."
    }

@router.post(
        "/login",
        response_model=TokenResponse,
        summary="로그인 및 토큰 발급",
        description="로그인을 하여 사용자에게 토큰을 발급합니다.")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """사용자 자격 증명을 확인하고 JWT 액세스 토큰을 발급합니다.

    FastAPI의 OAuth2PasswodRequestForm을 사용하여
    application/x-www-form-urlencoded 형식으로 데이터를 받습니다.

    Args:
        form_data (OAuth2PasswordRequestForm): 클라이언트가 전달한 username과 password

    Returns:
        TokenResponse: 발급된 JWT 액세스 토큰과 토큰 타입(bearer)
    """

    """
    TODO: [?] 로그인 및 토큰 발급 로직
    1. crud.auth.authenticate_user(form_data.username, form_data.password) 호출
    2. 인증이 성공적으로 끝나면, core.security.create_access_token({"sub": form_data.username}) 호출
    3. 반환받은 토큰 문자열을 아래 딕셔너리에 담아서 리턴
    core.security.create_access_token() 호출하여 토큰 생성
    """
    return {
        "access_token": "dummy_jwt_token",
        "token_type" : "bearer"
    }


@router.post(
        "/logout",
        summary="로그아웃 및 토큰 삭제 유도 응답",
        description="로그아웃을 하여 사용자가 토큰을 삭제하도록 유도합니다.")
def logout():
    """현재 로그인된 사용자의 로그아웃 처리를 수행합니다.

    JWT는 무상태(Stateless) 토큰이므로, 서버 측 세션 삭제 대신
    클라이언트에게 토큰 삭제를 유도하는 응답을 보냅니다.

    Returns:
        dict: 로그아웃 성공 메시지
    """
    
    """
    # TODO: [?] 로그아웃 로직 (필요시 블랙리스트 처리 구현)
    현재는 Frontend에서 토큰을 지우도록 유도하는 메시지만 반환하면 됨
    """
    return {
        "message" : "로그아웃 되었습니다."
    }