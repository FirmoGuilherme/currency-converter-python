from datetime import datetime
from sqlalchemy.orm import Session

from ..error.exceptions import UserNotFoundError
from ..models.transaction import Transaction
from ..connectors.currency_api import CurrencyAPIConnector
from .user import UserRepository

class TransactionRepository:

	@staticmethod
	def find_all(db: Session) -> list[Transaction]:
		return db.query().all()

	@staticmethod
	def save(db: Session, transaction: Transaction) -> Transaction:
		if not UserRepository.find_by_id(db, transaction.user_id):
			raise UserNotFoundError(transaction.user_id)
		currency_client = CurrencyAPIConnector()
		converted_value, rate = currency_client.convert(transaction.from_value ,
		                                                transaction.from_currency,
		                                                transaction.to_currency)
		transaction.to_value = converted_value
		transaction.rate = rate
		transaction.timestamp = datetime.now()
		db.add(transaction)
		db.commit()
		return transaction

	@staticmethod
	def find_by_user_id(db: Session, user_id: int) -> Transaction:
		user = db.query(Transaction).filter(Transaction.user_id == user_id).all()
		if not user:
			raise UserNotFoundError(user_id)
		return user
