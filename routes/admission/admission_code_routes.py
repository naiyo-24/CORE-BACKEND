from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy.orm import Session
from datetime import datetime

from db import get_db
from models.admission.admission_code_models import AdmissionCode
from models.auth.counsellor_models import Counsellor

router = APIRouter(prefix="/api/admission-codes", tags=["AdmissionCodes"])


class AdmissionCodeBase(BaseModel):
    admission_code: str
    counsellor_id: str


class AdmissionCodeCreate(AdmissionCodeBase):
    pass


class AdmissionCodeUpdate(BaseModel):
    counsellor_id: Optional[str] = None


class AdmissionCodeResponse(AdmissionCodeBase):
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


@router.post("/create", response_model=AdmissionCodeResponse, status_code=status.HTTP_201_CREATED)
def create_admission_code(payload: AdmissionCodeCreate, db: Session = Depends(get_db)):
    # ensure counsellor exists
    counsellor = db.query(Counsellor).filter_by(counsellor_id=payload.counsellor_id).first()
    if not counsellor:
        raise HTTPException(status_code=404, detail="Counsellor not found")

    # check duplicate admission code
    if db.query(AdmissionCode).filter_by(admission_code=payload.admission_code).first():
        raise HTTPException(status_code=409, detail="Admission code already exists")

    now = datetime.utcnow()
    ac = AdmissionCode(
        admission_code=payload.admission_code,
        counsellor_id=payload.counsellor_id,
        created_at=now,
        updated_at=now,
    )
    db.add(ac)
    db.commit()
    db.refresh(ac)
    return ac


@router.get("/get-all", response_model=List[AdmissionCodeResponse])
def get_all_admission_codes(db: Session = Depends(get_db)):
    items = db.query(AdmissionCode).all()
    return items


@router.get("/get-by/{admission_code}", response_model=AdmissionCodeResponse)
def get_admission_code(admission_code: str, db: Session = Depends(get_db)):
    item = db.query(AdmissionCode).filter_by(admission_code=admission_code).first()
    if not item:
        raise HTTPException(status_code=404, detail="Admission code not found")
    return item


@router.put("/put-by/{admission_code}", response_model=AdmissionCodeResponse)
def update_admission_code(admission_code: str, payload: AdmissionCodeUpdate, db: Session = Depends(get_db)):
    item = db.query(AdmissionCode).filter_by(admission_code=admission_code).first()
    if not item:
        raise HTTPException(status_code=404, detail="Admission code not found")

    if payload.counsellor_id is not None:
        counsellor = db.query(Counsellor).filter_by(counsellor_id=payload.counsellor_id).first()
        if not counsellor:
            raise HTTPException(status_code=404, detail="Counsellor not found")
        item.counsellor_id = payload.counsellor_id

    item.updated_at = datetime.utcnow()
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@router.delete("/delete-by/{admission_code}", response_model=dict)
def delete_admission_code(admission_code: str, db: Session = Depends(get_db)):
    item = db.query(AdmissionCode).filter_by(admission_code=admission_code).first()
    if not item:
        raise HTTPException(status_code=404, detail="Admission code not found")
    db.delete(item)
    db.commit()
    return {"detail": "Deleted successfully"}
