#this file is responsible for signing, encodeng, decodeing and returninig JWTs.
import datetime
import jwt
from decouple import config

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")
EXPIRY_SECONDS = 20

#returns the generated tokens (JWTs)
def token_response(token: str):
    return {
        "accessToken" : token,
        "roles": "*"
    }

def signJWT(userID: str):
    payload = {
        "userID": userID,
        "exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(seconds=EXPIRY_SECONDS)
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)


def decodeJWT(token: str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return decode_token if decode_token['expires'] >= datetime.datetime.now(tz=datetime.timezone.utc) else None
    except:
        return {}