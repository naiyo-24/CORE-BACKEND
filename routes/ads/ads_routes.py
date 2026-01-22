from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form, status
from sqlalchemy.orm import Session
from typing import List, Optional
import os
import shutil
from db import get_db
from models.ads.ads_models import Advertisement
from pydantic import BaseModel
from datetime import datetime

router = APIRouter(prefix="/api/ads", tags=["Advertisements"])

# Pydantic Schemas
class AdvertisementBase(BaseModel):
	headline: str
	tagline: Optional[str] = None
	website_link: Optional[str] = None
	active_status: Optional[bool] = True

class AdvertisementCreate(AdvertisementBase):
	pass

class AdvertisementUpdate(AdvertisementBase):
	pass

class AdvertisementOut(AdvertisementBase):
	id: int
	ad_image: Optional[str]
	created_at: datetime
	updated_at: Optional[datetime]

	class Config:
		from_attributes = True

# Helper for image upload path
def save_ad_image(ad_id: int, file: UploadFile) -> str:
	upload_dir = f"uploads/ads/{ad_id}"
	os.makedirs(upload_dir, exist_ok=True)
	file_path = os.path.join(upload_dir, file.filename)
	with open(file_path, "wb") as buffer:
		shutil.copyfileobj(file.file, buffer)
	return file_path

# Create Advertisement
@router.post("/create", response_model=AdvertisementOut, status_code=status.HTTP_201_CREATED)
async def create_advertisement(
	headline: str = Form(...),
	tagline: Optional[str] = Form(None),
	website_link: Optional[str] = Form(None),
	active_status: Optional[bool] = Form(True),
	ad_image: Optional[UploadFile] = File(None),
	db: Session = Depends(get_db)
):
	ad = Advertisement(
		headline=headline,
		tagline=tagline,
		website_link=website_link,
		active_status=active_status
	)
	db.add(ad)
	db.commit()
	db.refresh(ad)
	# Save image if provided
	if ad_image:
		file_path = save_ad_image(ad.id, ad_image)
		ad.ad_image = file_path
		db.commit()
		db.refresh(ad)
	return ad

# Get all advertisements
@router.get("/get-all", response_model=List[AdvertisementOut])
def get_all_ads(db: Session = Depends(get_db)):
	return db.query(Advertisement).all()

# Get advertisement by id
@router.get("/get-by/{ad_id}", response_model=AdvertisementOut)
def get_ad_by_id(ad_id: int, db: Session = Depends(get_db)):
	ad = db.query(Advertisement).filter(Advertisement.id == ad_id).first()
	if not ad:
		raise HTTPException(status_code=404, detail="Advertisement not found")
	return ad

# Update advertisement by id
@router.put("/put-by/{ad_id}", response_model=AdvertisementOut)
async def update_ad_by_id(
	ad_id: int,
	headline: str = Form(...),
	tagline: Optional[str] = Form(None),
	website_link: Optional[str] = Form(None),
	active_status: Optional[bool] = Form(True),
	ad_image: Optional[UploadFile] = File(None),
	db: Session = Depends(get_db)
):
	ad = db.query(Advertisement).filter(Advertisement.id == ad_id).first()
	if not ad:
		raise HTTPException(status_code=404, detail="Advertisement not found")
	ad.headline = headline
	ad.tagline = tagline
	ad.website_link = website_link
	ad.active_status = active_status
	if ad_image:
		file_path = save_ad_image(ad.id, ad_image)
		ad.ad_image = file_path
	db.commit()
	db.refresh(ad)
	return ad

# Delete advertisement by id
@router.delete("/delete-by/{ad_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_ad_by_id(ad_id: int, db: Session = Depends(get_db)):
	ad = db.query(Advertisement).filter(Advertisement.id == ad_id).first()
	if not ad:
		raise HTTPException(status_code=404, detail="Advertisement not found")
	db.delete(ad)
	db.commit()
	# Optionally, delete image folder
	upload_dir = f"uploads/ads/{ad_id}"
	if os.path.exists(upload_dir):
		shutil.rmtree(upload_dir)
	return

# Bulk delete advertisements
class BulkDeleteRequest(BaseModel):
	ids: List[int]

@router.delete("/delete/bulk", status_code=status.HTTP_204_NO_CONTENT)
def bulk_delete_ads(request: BulkDeleteRequest, db: Session = Depends(get_db)):
	ads = db.query(Advertisement).filter(Advertisement.id.in_(request.ids)).all()
	for ad in ads:
		db.delete(ad)
		# Optionally, delete image folder
		upload_dir = f"uploads/ads/{ad.id}"
		if os.path.exists(upload_dir):
			shutil.rmtree(upload_dir)
	db.commit()
	return
