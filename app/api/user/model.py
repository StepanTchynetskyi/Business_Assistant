import uuid

from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import UUID

from app.db import database as db


class User(db.Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    name = Column(String)
    last_name = Column(String)
    to_delete = Column(String)
    is_active = Column(Boolean, default=True)
