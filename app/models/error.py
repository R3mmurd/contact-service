from pydantic import BaseModel
from typing import Optional, Any


class Error(BaseModel):
    code: str
    title: str
    detail: Optional[str] = None


class ErrorResponse(BaseModel):
    errors: list[Error]

    def add_error(self, code: str, title: str, detail: Optional[str] = None) -> None:
        error = Error(code=code, title=title, detail=detail)
        self.errors.append(error)
