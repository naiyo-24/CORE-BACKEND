from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from db import Base

# SalarySlip model for storing salary slip records
class SalarySlip(Base):
	__tablename__ = "salary_slips"

	id = Column(Integer, primary_key=True, index=True)
	teacher_id = Column(String, ForeignKey("teachers.teacher_id"), nullable=False)
	transaction_id = Column(String, nullable=False)
	month = Column(String, nullable=False)
	year = Column(Integer, nullable=False)
	basic_salary = Column(Float, nullable=False)
	pa = Column(Float, nullable=True)
	da = Column(Float, nullable=True)
	deductions = Column(Float, nullable=True)
	provident_fund = Column(Float, nullable=True)
	si = Column(Float, nullable=True)
	total_compensation = Column(Float, nullable=False)
	pdf_path = Column(String, nullable=False)
	created_at = Column(DateTime, default=datetime.utcnow)
	updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

	# Relationship to Teacher
	teacher = relationship("Teacher", backref="salary_slips")
