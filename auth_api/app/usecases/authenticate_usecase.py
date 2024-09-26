from app.gateways.user_repository_gateway import UserRepositoryGateway
from app.entities.http.http_response import HttpResponse
from app.utils.hash_manager import HashManager
from app.utils.token_manager import TokenManager
from app.entities.dto.user_dto import UserDTO
from app.entities.dto.passwords import ResetPassword, ChangePassword
from http import HTTPStatus


class AuthenticateUseCase:
    def __init__(self, user_repository: UserRepositoryGateway) -> None:
        self.user_repository = user_repository

    def authenticate_user(self, email: str, raw_password: str) -> HttpResponse:
        user = self.user_repository.get_user_by_email(email)
        if user is None:
            return HttpResponse(status_code=HTTPStatus.NOT_FOUND, content={"detail": f"{email} has not been found!"})
        
        user_dto = UserDTO(
            email=user.email,
            group_id=user.group_id,
            id=user.id,
            name=user.name,
            password=user.password
        )
        
        if HashManager.verify_hash(raw_password, user_dto.password):
            token = TokenManager.generate_token({"user_id": user_dto.id})
            refresh_token = TokenManager.generate_new_refresh_token({"user_id": user_dto.id})
            return HttpResponse(status_code=HTTPStatus.OK, content={"access_token": token, "refresh_token": refresh_token, "type": "bearer"},)
        return HttpResponse(status_code=HTTPStatus.UNAUTHORIZED, content={"detail": f"invalid credentials!"},)

    def refresh_token(self, token: str) -> HttpResponse:
        if not TokenManager.is_valid(token):
            return HttpResponse(HTTPStatus.UNAUTHORIZED, {"detail": "invalid or expired token"})
        return HttpResponse(HTTPStatus.OK, {
            "access_token": TokenManager.refresh_token(token),
            "type": "bearer"
        })
    
    
    def reset_password(self, body: ResetPassword) -> HttpResponse:
        pass

    def change_password(self, body: ChangePassword) -> HttpResponse:
        user = self.user_repository.get_user_by_email(body.email)
        if user is None:
            return HttpResponse(HTTPStatus.NOT_FOUND, {"detail": "user not found"})
        
        if HashManager.verify_hash(body.old_password, user.password):
            new_password = HashManager.hash_password(body.new_password)
            result = self.user_repository.change_password(user.id, new_password)
            if result is None:
                return HttpResponse(HTTPStatus.BAD_REQUEST, {"detail": "something went wrong"})
            
            return HttpResponse(HTTPStatus.OK, {"message": "password changed successfully!"})
        return HttpResponse(HTTPStatus.UNAUTHORIZED, {"detail": "invalid credentials"})