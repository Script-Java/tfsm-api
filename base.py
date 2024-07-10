from pydantic import BaseModel, EmailStr, constr
from datetime import datetime

class ContactClientBase(BaseModel):
    first_name: constr(min_length=1, max_length=55)
    last_name: constr(min_length=1, max_length=55)
    email: EmailStr
    phone: constr(min_length=1, max_length=55)
    message: constr(min_length=1)

class ContactClientCreate(ContactClientBase):
    pass

class ContactClient(ContactClientBase):
    id: int
    created: datetime

    class Config:
        orm_mode = True

class PhoneSchedulerBase(BaseModel):
    first_name: constr(min_length=1, max_length=55)
    last_name: constr(min_length=1, max_length=55)
    phone: constr(min_length=1, max_length=55)
    time: constr(min_length=1, max_length=55)

class PhoneSchedulerCreate(PhoneSchedulerBase):
    pass

class PhoneScheduler(PhoneSchedulerBase):
    id: int
    created: datetime

    class Config:
        orm_mode = True
