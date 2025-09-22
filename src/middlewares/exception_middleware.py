from starlette.middleware.base import BaseHTTPMiddleware
from src.error.exceptions import GenericError
from src.error.error_handlers import handle_exception


class ExceptionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        try:
            response = await call_next(request)
            return response
        except GenericError as exc:
            return handle_exception(exc)
