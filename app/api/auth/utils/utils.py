import os

from passlib.context import CryptContext

from app.api.user import models as user_models
from app.utils.custom_exceptions import LoginException
import jwt
from datetime import datetime, timedelta
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def hash_password(plain_password):
    return pwd_context.hash(plain_password)


def verify_user(email, user_password, db):
    user = db.query(user_models.User).filter(user_models.User.email == email).first()
    if not user:
        raise LoginException()
    if not verify_password(user_password, user.password):
        raise LoginException()
    return user


def create_access_token(user):
    try:
        payload = {"sub": str(user.id),
                   "user_email": user.email,
                   "exp": datetime.utcnow() + timedelta(minutes=120)}
        return jwt.encode(payload, os.environ.get("JWT_SECRET_KEY"), algorithm="HS256")
    except Exception as err:
        raise err
