from fastapi import Depends, APIRouter
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.api.auth import schemas as auth_schemas
from app.api.auth.utils import utils
from app.api.user import models as user_models
from app.db import database

oauth_bearer = OAuth2PasswordBearer(tokenUrl="login")
router = APIRouter()


@router.post("/register", response_model=auth_schemas.CreatedUser, status_code=201)
def register(user_data: auth_schemas.CreateUser, db: Session = Depends(database.get_db)):
    user_data.password = utils.hash_password(user_data.password)
    user = user_models.User(**user_data.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user.__dict__


@router.post("/login", response_model=auth_schemas.Token, status_code=200)
def login(user_data: auth_schemas.LoginForm, db: Session = Depends(database.get_db)):
    user = utils.verify_user(user_data.email, user_data.password, db)
    token = utils.create_access_token(user)
    return {"access_token": token}


# @router.get("/try", dependencies=[Depends(oauth_bearer)])
# def try_user(db: Session = Depends(database.get_db)):
#     user = db.query(user_models.User).filter(user_models.User.email == "email1").first()
#     return {"user": user.__dict__}
