import pytest
from unittest.mock import MagicMock, patch
from src.models.transaction import Transaction
from src.repositories.transaction import TransactionRepository
from src.error.exceptions import UserNotFoundError

def test_save_transaction_unitario():
    mock_db = MagicMock()

    with patch("src.repositories.user.UserRepository.find_by_id") as mock_find_user, \
         patch("src.connectors.currency_api.CurrencyAPIConnector.convert") as mock_convert:

        mock_find_user.return_value = True
        mock_convert.return_value = (200.0, 2.0)

        transaction = Transaction(
            user_id=1,
            from_value=100.0,
            from_currency="USD",
            to_currency="BRL"
        )

        result = TransactionRepository.save(mock_db, transaction)

        assert result.to_value == 200.0
        assert result.rate == 2.0
        mock_db.add.assert_called_once_with(transaction)
        mock_db.commit.assert_called_once()



def test_find_by_user_id_success():
    mock_db = MagicMock()

    mock_db.query().filter().all.return_value = [
        Transaction(user_id=1, from_value=100.0, to_value=500.0, rate=5.0)
    ]

    result = TransactionRepository.find_by_user_id(mock_db, user_id=1)

    assert isinstance(result, list)
    assert result[0].user_id == 1
    assert result[0].to_value == 500.0




def test_find_by_user_id_not_found():
    mock_db = MagicMock()
    mock_db.query().filter().all.return_value = []

    with pytest.raises(UserNotFoundError) as exc_info:
        TransactionRepository.find_by_user_id(mock_db, user_id=99)

    assert str(exc_info.value) == "User with id 99 not found"