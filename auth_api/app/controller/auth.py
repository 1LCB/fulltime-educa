from fastapi import status, Depends, APIRouter, Header, HTTPException
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from app.usecases.authenticate_usecase import AuthenticateUseCase
from app.entities.dto.passwords import ChangePassword, ResetPassword
from infrastructure.database.mysql.repository.users_repository import UserRepository
from app.utils.token_manager import TokenManager


router = APIRouter(prefix="/api/auth", tags=["Auth"])

oauth2 = OAuth2PasswordBearer("/api/auth/authenticate")
get_usecase = lambda: AuthenticateUseCase(user_repository=UserRepository())


def token_validation(token = Depends(oauth2)):
    if not TokenManager.is_valid(token):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid or expired token!")


@router.post("/authenticate",status_code=status.HTTP_200_OK,)
async def authenticate(form_data: OAuth2PasswordRequestForm = Depends(), usecase: AuthenticateUseCase = Depends(get_usecase)) -> None:
    response = usecase.authenticate_user(form_data.username, form_data.password)
    return JSONResponse(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
    )


@router.post("/refresh", status_code=status.HTTP_200_OK)
async def refresh_token(token=Header(), usecase: AuthenticateUseCase = Depends(get_usecase)) -> None:
    response = usecase.refresh_token(token)
    return JSONResponse(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
    )


@router.post("/reset-password", status_code=status.HTTP_200_OK)
async def reset_password(body: ResetPassword, usecase: AuthenticateUseCase = Depends(get_usecase)):
    response = usecase.reset_password(body)
    return JSONResponse(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
    )


@router.post("/change-password", status_code=status.HTTP_200_OK)
async def change_password(body: ChangePassword, usecase: AuthenticateUseCase = Depends(get_usecase)):
    response = usecase.change_password(body)
    return JSONResponse(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
    )
