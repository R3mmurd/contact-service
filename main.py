import uvicorn
from fastapi import FastAPI
from config import settings
from app.controllers.contact_form_controller import router as contact_form_router
from app.exceptions.api_exception import APIException, register_exception_handlers

app = FastAPI(title="Contact Form API", version="1.0.0")

register_exception_handlers(app)
app.include_router(contact_form_router, prefix="", tags=["Contact Form"])

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.app_host,
        port=settings.app_port,
        reload=True
    )
