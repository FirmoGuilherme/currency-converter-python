from datetime import datetime
from sqlalchemy.orm import Session

from ..error.exceptions import UserNotFoundError
from ..models.user import User


class UserRepository:

	@staticmethod
	def save(db: Session, user: User) -> User:
		if user.id:
			user.updated_at = datetime.now()
			user.created_at = db.query(User).get(user.id).created_at
			db.merge(user)
		else:
			user.created_at = datetime.now()
			db.add(user)
		db.commit()
		return user

	@staticmethod
	def find_by_id(db: Session, user_id: int) -> User:
		user = db.query(User).filter(User.id == user_id).first()
		if not user:
			raise UserNotFoundError(user_id)
		return user
