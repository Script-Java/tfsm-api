from sqlalchemy import Column, Text, DateTime, Integer, String
from database import Base
import datetime

class ContactClinet(Base):
    __tablename__ = 'ContactClient'
    
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(55), nullable=False, index=True)
    last_name = Column(String(55), nullable=False, index=True)
    email = Column(String(255), nullable=False, index=True)
    phone = Column(String(55), nullable=False, index=True)
    message = Column(Text, nullable=False, index=True)
    created = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    
    def to_json(self):
        return {
        'id': self.id,
        'first_name': self.first_name,
        'last_name': self.last_name,
        'email': self.email,
        'phone': self.phone,
        'message': self.message,
        'created': self.created
    
    }
    
class PhoneScheduler(Base):
    __tablename__ = 'PhoneScheduler'
    
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(55), nullable=False, index=True)
    last_name = Column(String(55), nullable=False, index=True)
    phone = Column(String(55), nullable=False, index=True)
    time = Column(String(55), nullable=False, index=True)
    created = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    
    def to_json(self):
        return {
        'id': self.id,
        'first_name': self.first_name,
        'last_name': self.last_name,
        'phone': self.phone,
        'time': self.time,
        'created': self.created
    
    }