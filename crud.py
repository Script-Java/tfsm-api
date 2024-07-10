from sqlalchemy.orm import Session
import models
import base

def create_contact_client(db: Session, contact_client: schemas.ContactClientCreate):
    db_contact_client = models.ContactClient(**contact_client.dict())
    db.add(db_contact_client)
    db.commit()
    db.refresh(db_contact_client)
    return db_contact_client

def create_phone_scheduler(db: Session, phone_scheduler: schemas.PhoneSchedulerCreate):
    db_phone_scheduler = models.PhoneScheduler(**phone_scheduler.dict())
    db.add(db_phone_scheduler)
    db.commit()
    db.refresh(db_phone_scheduler)
    return db_phone_scheduler

def get_contact_client(db: Session, contact_client_id: int):
    return db.query(models.ContactClient).filter(models.ContactClient.id == contact_client_id).first()

def get_phone_scheduler(db: Session, phone_scheduler_id: int):
    return db.query(models.PhoneScheduler).filter(models.PhoneScheduler.id == phone_scheduler_id).first()
