import pytest
import datetime
from unittest.mock import patch
from app.main import outdated_products


@pytest.fixture
def product_list() -> list[dict]:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]


def test_expiration_day_today_not_outdated(product_list: list) -> None:
    today = datetime.date(2022, 2, 10)
    with patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = today
        result = outdated_products(product_list)
        assert result == ["chicken", "duck"]


def test_expiration_day_yesterday_outdated(product_list: list) -> None:
    yesterday = datetime.date(2022, 2, 2)
    with patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = yesterday
        result = outdated_products(product_list)
        assert result == ["duck"]
