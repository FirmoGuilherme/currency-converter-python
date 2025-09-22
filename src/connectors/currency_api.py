import requests
from ..constants import CURRENCY_API_KEY, CURRENCY_API_URL
from ..helpers import handle_exception

class CurrencyAPIConnector:
    def __init__(self):
        self.url = CURRENCY_API_URL
        self.headers = {"apikey": CURRENCY_API_KEY}

    def convert(self, amount, from_currency, to_currency):
        params = {"base_currency": from_currency, "currencies": to_currency}
        response = requests.get(self.url, headers=self.headers, params=params)
        handle_exception(response, params, self.url)
        json_response = response.json()
        rate = json_response["data"][to_currency]["value"]
        return amount * rate, rate