from sqlalchemy import Column, Integer, Text, DateTime
from sqlalchemy.sql import func
from db import Base


class HelpCenter(Base):
    __tablename__ = "help_center"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    report_id = Column(Text, nullable=False, unique=True, index=True)
    name = Column(Text, nullable=True)
    phone_no = Column(Text, nullable=True)
    email = Column(Text, nullable=True)
    problem_description = Column(Text, nullable=True)
    status = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
