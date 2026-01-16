from sqlalchemy import Column, String, DateTime, JSON, Text
from db import Base
from datetime import datetime


class Classroom(Base):
    __tablename__ = "classrooms"

    classroom_id = Column(String, primary_key=True, index=True)
    class_name = Column(String, nullable=True)
    teacher_id = Column(String, nullable=False, index=True)
    course_id = Column(String, nullable=False, index=True)
    # list of student ids
    students = Column(JSON, nullable=True)
    # list of dicts for daily content items:
    # [{"date":"ISO8601","heading":"title","description":"text","link":"https://..."}, ...]
    daily_links = Column(JSON, nullable=True)
    # one or more teacher admins for the class (list of teacher_ids)
    admins = Column(JSON, nullable=True)
    # optional classroom photo (file path or URL)
    classroom_photo = Column(String, nullable=True)
    # optional classroom description
    description = Column(Text, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<Classroom(classroom_id={self.classroom_id}, teacher_id={self.teacher_id}, course_id={self.course_id}, admins={self.admins})>"
