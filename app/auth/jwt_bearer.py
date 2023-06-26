# verify to check if request is Authorized or not

from typing import Any, Coroutine, Optional
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.security.http import HTTPAuthorizationCredentials
from starlette.requests import Request
from .jwt_handler import decode_jwt


class jwtBearer(HTTPBearer):
    def __init__(self, auto_Error: bool = True):
        super(jwtBearer, self).__init__(auto_error=auto_Error)

    async def __call__(self, request: Request) -> Coroutine[Any, Any, HTTPAuthorizationCredentials | None]:
        credentials: HTTPAuthorizationCredentials = await super(jwtBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == 'Bearer':
                raise HTTPException(status_code=404, detail='Invalid Token')
            else:
                return credentials.credentials
        else:
            raise HTTPException(status_code=404, detail='Invalid Token')

    def verify_jwt(self, jwt_token: str):
        isTokenValid: bool = False
        payload = decode_jwt(jwt_token)
        if payload:
            isTokenValid = True
        return isTokenValid
