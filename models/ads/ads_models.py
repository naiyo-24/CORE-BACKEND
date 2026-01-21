from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from db import Base

class Advertisement(Base):
	__tablename__ = "advertisements"

	id = Column(Integer, primary_key=True, index=True)
	headline = Column(String(255), nullable=False)
	tagline = Column(String(255), nullable=True)
	website_link = Column(String(512), nullable=True)
	ad_image = Column(String(512), nullable=True)  # Path to image file
	created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
	updated_at = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now(), nullable=False)
	active_status = Column(Boolean, default=True, nullable=False)
