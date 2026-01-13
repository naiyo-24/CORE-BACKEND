from sqlalchemy import Column, String, Text, Boolean, JSON, UniqueConstraint
from db import Base

class Course(Base):
    __tablename__ = "courses"
    __table_args__ = (
        UniqueConstraint('course_code', 'course_category', name='uix_course_code_category'),
    )

    # Primary key
    course_id = Column(String, primary_key=True, index=True)

    # Common fields
    course_name = Column(String, nullable=False)
    course_description = Column(Text)
    course_code = Column(String, nullable=False, index=True)
    weight_requirements = Column(String)
    height_requirements = Column(String)
    vision_standards = Column(String)
    medical_requirements = Column(Text)
    min_educational_qualification = Column(String)
    age_criteria = Column(String)
    internship_included = Column(Boolean, default=False)
    installment_available = Column(Boolean, default=False)
    installment_policy = Column(Text)
    course_category = Column(String, nullable=False)  # "general" or "executive"
    course_photo = Column(String)  # File path
    course_video = Column(String)  # File path

    # JSONB column for category-specific data
    category_data = Column(JSON, nullable=False)
    # Expected structure:
    # {
    #   "job_roles_offered": str,
    #   "placement_assistance": bool,
    #   "placement_type": str,  # "Assisted" or "Guaranteed"
    #   "placement_rate": float,
    #   "advantages_highlights": str,
    #   "course_fees": float,
    #   "created_at": str,
    #   "updated_at": str,
    #   "active_status": bool
    # }

    def __repr__(self):
        return f"<Course(course_id={self.course_id}, course_name={self.course_name}, category={self.course_category})>"
