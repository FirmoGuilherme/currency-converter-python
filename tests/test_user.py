from unittest.mock import MagicMock
from src.models.user import User
from src.repositories.user import UserRepository

def test_save_user_novo():
    mock_db = MagicMock()
    user = User(name="Teste")

    result = UserRepository.save(mock_db, user)

    mock_db.add.assert_called_once_with(user)
    mock_db.commit.assert_called_once()
    assert result.created_at is not None