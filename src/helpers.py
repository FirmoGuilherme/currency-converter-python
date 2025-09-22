from .error.exceptions import RequestError

def handle_exception(request, payload, url):
	if request.status_code in range(201, 401):
		msg = request.json().get("message")
		logging.error(msg)
		raise RequestError(url, payload, message)

	if request.status_code >= 500:
		msg = request.json().get("message")
		logging.error(msg)
		raise RequestError(url, payload, message)