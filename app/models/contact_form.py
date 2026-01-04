from pydantic import BaseModel, EmailStr


class ContactForm(BaseModel):
    email: EmailStr
    subject: str
    message: str
