from fastapi import APIRouter
from app.models.contact_form import ContactForm
from app.services.contact_form_service import ContactFormService

router = APIRouter()


@router.post("/contacts", status_code=204)
async def submit_contact_form(contact_form: ContactForm):
    await ContactFormService.process_contact_form(contact_form)
    return
