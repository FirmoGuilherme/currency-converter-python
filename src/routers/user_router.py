from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import Annotated
from src.connectors.db import get_db
from src.models.user import User
from src.schemas.user import UserRequest, UserResponse
from src.repositories.user import UserRepository
from src.logging import get_logger

logger = get_logger(__name__)
router = APIRouter()

db_dependency = Annotated[Session, Depends(get_db)]

@router.post("", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(request: UserRequest, db: db_dependency):
    logger.info(f"Creating user {request.dict()}")
    user = UserRepository.save(db, User(**request.dict()))
    logger.info(f"User created with id {user.id!r}")
    return UserResponse.from_orm(user)
