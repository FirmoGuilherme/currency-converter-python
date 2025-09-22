class GenericError(Exception):

	def __init__(self, msg: str, status_code: int = 500):
		self.message = msg
		super().__init__(self.message)

	def to_json(self) -> dict:
		excp_data = {
			'message': self.message
		}
		return excp_data


class RequestError(GenericError):

	def __init__(self, endpoint, payload, api_response):
		self.endpoint = endpoint
		self.payload = payload
		self.api_response = api_response
		super().__init__(f'Request Error on {endpoint!r} with payload {payload}')

	def to_json(self):
		data = super().to_json()
		data['api_response'] = self.api_response
		data['endpoint'] = self.endpoint
		data['payload'] = self.payload
		return data


class UserNotFoundError(GenericError):

	def __init__(self, user_id: int):
		self.user_id = user_id
		super().__init__(f'User with id {user_id!r} not found')
