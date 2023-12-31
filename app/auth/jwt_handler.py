# responsible for signing, encoding, decoding and return JWTs
import time
import jwt
from decouple import config

JWT_SECRET = config('SECRET')
JWT_ALGORITHM = config('ALGORITHM')


def token_response(token: str):
    return {'access token': token}


def sign_jwt(userID: str):
    payload = {
        'userID': userID,
        'expiry': time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)


def decode_jwt(token: str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return decode_token if decode_token['expires'] >= time.time() else None
    except:
        return {}
