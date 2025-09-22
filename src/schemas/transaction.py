from pydantic import BaseModel, Field
from datetime import datetime
from typing import List
from enum import Enum


class AcceptedCurrencies(str, Enum):
	USD = "USD"
	BRL = "BRL"
	EUR = "EUR"
	JPY = "JPY"


class TransactionRequest(BaseModel):
	user_id: int
	from_currency: AcceptedCurrencies
	to_currency: AcceptedCurrencies
	from_value: float = Field(alias="value")


class TransactionResponse(BaseModel):
	id: int
	user_id: int
	from_currency: str
	to_currency: str
	from_value: float
	to_value: float
	rate: float
	timestamp: datetime

	class Config:
		orm_mode = True
		from_attributes=True
