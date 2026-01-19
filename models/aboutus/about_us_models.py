from sqlalchemy import Column, Integer, Text
from db import Base


class AboutUs(Base):
    __tablename__ = "about_us"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    mission = Column(Text, nullable=True)
    vision = Column(Text, nullable=True)
    placement_rate = Column(Text, nullable=True)
    experience = Column(Text, nullable=True)
    partner = Column(Text, nullable=True)
    courses = Column(Text, nullable=True)
    director_quote = Column(Text, nullable=True)
    website = Column(Text, nullable=True)
    office_address = Column(Text, nullable=True)
    phone_no = Column(Text, nullable=True)
    email = Column(Text, nullable=True)
