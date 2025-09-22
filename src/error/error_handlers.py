import logging
import traceback
from .exceptions import *
from fastapi.responses import JSONResponse
from fastapi import Request, FastAPI
from fastapi.exceptions import RequestValidationError

def handle_exception(excp):


    def handle_request_error(exc: RequestError):
        return JSONResponse(
            status_code=400,
            content=exc.to_json()
        )

    def handle_user_not_found_error(exc: UserNotFoundError):
        return JSONResponse(
            status_code=404,
            content=exc.to_json()
        )

    def handle_generic(exc: Exception):
        traceback_str = traceback.format_exc()
        logging.exception(traceback_str)
        return JSONResponse(
            status_code=500,
            content={
                "stacktrace": traceback_str,
                "message": str(exc)
            }
        )

    exception_handlers = {
        UserNotFoundError: handle_user_not_found_error,
        RequestError: handle_request_error
    }

    logging.exception(excp)
    return exception_handlers.get(type(excp), handle_generic)(excp)

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = []
    for err in exc.errors():
        errors.append({
            "field": ".".join(str(loc) for loc in err["loc"]),
            "message": err["msg"]
        })
    return JSONResponse(
        status_code=422,
        content={
            "error": "Validation error",
            "details": errors
        },
    )


def register_error_handlers(app: FastAPI):
    app.add_exception_handler(RequestValidationError, validation_exception_handler)