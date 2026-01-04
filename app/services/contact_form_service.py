from fastapi import HTTPException
import httpx
from config import settings
from app.models.contact_form import ContactForm
from app.exceptions.api_exception import APIException


class ContactFormService:
    TELEGRAM_API_URL = f"https://api.telegram.org/bot{settings.telegram_bot_token}/sendMessage"

    @staticmethod
    async def process_contact_form(contact_form: ContactForm):
        if not contact_form.email or not contact_form.subject or not contact_form.message:
            raise APIException(
                error_code="E0001",
                message="All fields are required.",
                status_code=400
            )

        message = (
            "*🚀Hola, se ha recibido un nuevo mensaje de contacto desde la web*\n\n"
            f"📧 *Email:* `{contact_form.email}`\n\n"
            f"📌 *Asunto:* {contact_form.subject}\n\n"
            f"📝 *Descripción:*\n_{contact_form.message}_"
        )

        payload = {
            "chat_id": settings.telegram_chat_id,
            "text": message,
            "parse_mode": "Markdown"
        }

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(ContactFormService.TELEGRAM_API_URL, json=payload)
                response.raise_for_status()
                return response.json()
            except httpx.HTTPStatusError as e:
                raise APIException(
                    error_code="E0002",
                    message="Failed to send message via Telegram.",
                    status_code=e.response.status_code,
                    details=e.response.text
                )
