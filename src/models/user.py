from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..connectors.db import Base


class User(Base):
	__tablename__ = 'user'

	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String)
