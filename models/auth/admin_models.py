from sqlalchemy import Column, String, DateTime
from datetime import datetime
from db import Base

class Admin(Base):
    __tablename__ = "admins"
    
    id = Column(String, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    def __repr__(self):
        return f"<Admin(id={self.id}, email={self.email})>"
