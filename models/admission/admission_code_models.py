from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from db import Base


class AdmissionCode(Base):
    __tablename__ = "admission_codes"

    # Use the admission code as primary key
    admission_code = Column(String, primary_key=True, index=True)

    # FK to counsellors table
    counsellor_id = Column(String, ForeignKey("counsellors.counsellor_id"), nullable=False, index=True)

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    counsellor = relationship("Counsellor", backref="admission_codes")

    def __repr__(self):
        return f"<AdmissionCode(admission_code={self.admission_code}, counsellor_id={self.counsellor_id})>"
