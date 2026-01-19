from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from sqlalchemy.orm import Session

from db import get_db
from models.aboutus.about_us_models import AboutUs

router = APIRouter(prefix="/api/aboutus", tags=["AboutUs"])


class AboutUsBase(BaseModel):
    mission: Optional[str] = None
    vision: Optional[str] = None
    placement_rate: Optional[str] = None
    experience: Optional[str] = None
    partner: Optional[str] = None
    courses: Optional[str] = None
    director_quote: Optional[str] = None
    website: Optional[str] = None
    office_address: Optional[str] = None
    phone_no: Optional[str] = None
    email: Optional[str] = None


class AboutUsCreate(AboutUsBase):
    pass


class AboutUsUpdate(AboutUsBase):
    pass


class AboutUsResponse(AboutUsBase):
    id: int

    class Config:
        from_attributes = True

# Create AboutUs entry
@router.post("/create", response_model=AboutUsResponse)
def create_aboutus(payload: AboutUsCreate, db: Session = Depends(get_db)):
    about = AboutUs(
        mission=payload.mission,
        vision=payload.vision,
        placement_rate=payload.placement_rate,
        experience=payload.experience,
        partner=payload.partner,
        courses=payload.courses,
        director_quote=payload.director_quote,
        website=payload.website,
        office_address=payload.office_address,
        phone_no=payload.phone_no,
        email=payload.email,
    )
    db.add(about)
    db.commit()
    db.refresh(about)
    return about

# List all AboutUs entries
@router.get("/get-all", response_model=List[AboutUsResponse])
def list_aboutus(db: Session = Depends(get_db)):
    items = db.query(AboutUs).all()
    return items

# Get AboutUs entry by ID
@router.get("/get-by/{about_id}", response_model=AboutUsResponse)
def get_aboutus(about_id: int, db: Session = Depends(get_db)):
    about = db.query(AboutUs).filter(AboutUs.id == about_id).first()
    if not about:
        raise HTTPException(status_code=404, detail="AboutUs entry not found")
    return about

# Update AboutUs entry by ID
@router.put("/update/{about_id}", response_model=AboutUsResponse)
def update_aboutus(about_id: int, payload: AboutUsUpdate, db: Session = Depends(get_db)):
    about = db.query(AboutUs).filter(AboutUs.id == about_id).first()
    if not about:
        raise HTTPException(status_code=404, detail="AboutUs entry not found")

    for key, value in payload.dict(exclude_unset=True).items():
        setattr(about, key, value)

    db.add(about)
    db.commit()
    db.refresh(about)
    return about

# Delete AboutUs entry by ID
@router.delete("/delete/{about_id}")
def delete_aboutus(about_id: int, db: Session = Depends(get_db)):
    about = db.query(AboutUs).filter(AboutUs.id == about_id).first()
    if not about:
        raise HTTPException(status_code=404, detail="AboutUs entry not found")
    db.delete(about)
    db.commit()
    return {"detail": "Deleted successfully"}
