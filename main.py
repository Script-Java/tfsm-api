from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine, get_db
import requests

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/contact_clients/", response_model=schemas.ContactClient)
def create_contact_client(contact_client: schemas.ContactClientCreate, db: Session = Depends(get_db)):
    return crud.create_contact_client(db=db, contact_client=contact_client)

@app.get("/contact_clients/{contact_client_id}", response_model=schemas.ContactClient)
def read_contact_client(contact_client_id: int, db: Session = Depends(get_db)):
    db_contact_client = crud.get_contact_client(db=db, contact_client_id=contact_client_id)
    if db_contact_client is None:
        raise HTTPException(status_code=404, detail="ContactClient not found")
    return db_contact_client

@app.post("/phone_schedulers/", response_model=schemas.PhoneScheduler)
def create_phone_scheduler(phone_scheduler: schemas.PhoneSchedulerCreate, db: Session = Depends(get_db)):
    return crud.create_phone_scheduler(db=db, phone_scheduler=phone_scheduler)

@app.get("/phone_schedulers/{phone_scheduler_id}", response_model=schemas.PhoneScheduler)
def read_phone_scheduler(phone_scheduler_id: int, db: Session = Depends(get_db)):
    db_phone_scheduler = crud.get_phone_scheduler(db=db, phone_scheduler_id=phone_scheduler_id)
    if db_phone_scheduler is None:
        raise HTTPException(status_code=404, detail="PhoneScheduler not found")
    return db_phone_scheduler

@app.post("/send_json/")
def send_json(item_id: int, url: str, item_type: str, db: Session = Depends(get_db)):
    if item_type == "contact_client":
        item = crud.get_contact_client(db=db, contact_client_id=item_id)
    elif item_type == "phone_scheduler":
        item = crud.get_phone_scheduler(db=db, phone_scheduler_id=item_id)
    else:
        raise HTTPException(status_code=400, detail="Invalid item type")
    
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    response = requests.post(url, json=item.to_dict())
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to send JSON")
    return {"detail": "JSON sent successfully", "response": response.json()}
