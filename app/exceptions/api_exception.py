from typing import Any
from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.models.error import ErrorResponse


class APIException(Exception):
    def __init__(
            self, error_code: str,
            message: str,
            status_code: int = 400,
            details: Any = None
    ):
        self.error_code = error_code
        self.message = message
        self.status_code = status_code
        self.details = details


async def api_exception_handler(request: Request, exc: APIException):
    error_response = ErrorResponse(errors=[])
    error_response.add_error(exc.error_code, exc.message, exc.details)
    return JSONResponse(
        status_code=exc.status_code,
        content=error_response.model_dump()
    )

async def validation_exception_handler(request, exc: RequestValidationError):
    error_response = ErrorResponse(errors=[])

    for error in exc.errors():
        field_name = str(error["loc"][-1])
        msg = error["msg"]
        error_response.add_error(
            code="E0003",
            title=f"Validation error on field '{field_name}'",
            detail=msg
        )

    return JSONResponse(
        status_code=400,
        content=error_response.model_dump()
    )

def register_exception_handlers(app):
    app.add_exception_handler(APIException, api_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    