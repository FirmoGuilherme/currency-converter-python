from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import Annotated
from src.connectors.db import get_db
from src.models.transaction import Transaction
from src.schemas.transaction import TransactionRequest, TransactionResponse
from src.repositories.transaction import TransactionRepository
from src.logging import get_logger

logger = get_logger(__name__)
router = APIRouter()

db_dependency = Annotated[Session, Depends(get_db)]

@router.post("", response_model=TransactionResponse, status_code=status.HTTP_201_CREATED)
def create_transaction(request: TransactionRequest, db: db_dependency):
    logger.info(f"Creating transaction {request.dict()}")
    transaction = TransactionRepository.save(db, Transaction(**request.dict()))
    logger.info(f"Transaction created with id {transaction.id!r}")
    return TransactionResponse.from_orm(transaction)


@router.get("", response_model=list[TransactionResponse])
def get_transactions(user_id: int, db: db_dependency):
    return TransactionRepository.find_by_user_id(db, user_id)
