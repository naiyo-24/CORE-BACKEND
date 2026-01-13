from sqlalchemy import Column, String, Text, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from db import Base

class Student(Base):
	__tablename__ = "students"

	student_id = Column(String, primary_key=True, index=True)
	full_name = Column(String, nullable=False)
	phone_no = Column(String, nullable=False)
	email = Column(String, nullable=False, unique=True, index=True)
	address = Column(Text, nullable=False)
	guardian_name = Column(String, nullable=False)
	guardian_mobile_no = Column(String, nullable=False)
	guardian_email = Column(String, nullable=True)
	course_availing = Column(String, ForeignKey("courses.course_id"), nullable=False)
	interests = Column(JSON, nullable=True)
	hobbies = Column(JSON, nullable=True)
	password = Column(String, nullable=False)
	profile_photo = Column(String, nullable=True)
	created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
	updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

	# Relationship to fetch course details
	course = relationship("Course", backref="students")

	def __repr__(self):
		return f"<Student(student_id={self.student_id}, full_name={self.full_name})>"
