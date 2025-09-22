from sqlalchemy import Column, Integer, String, TIMESTAMP, Float, ForeignKey
from ..connectors.db import Base


class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    from_currency = Column(String)
    to_currency = Column(String)
    from_value = Column(Float)
    to_value = Column(Float)
    rate = Column(Float)
    timestamp = Column(TIMESTAMP)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
