from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional

from db import get_db
from models.auth.admin_models import Admin
from services.admin_id_generator import generate_admin_id

router = APIRouter(
    prefix="/api/admin",
    tags=["Admin"]
)

# Pydantic models for request/response
class AdminCreate(BaseModel):
    email: EmailStr
    password: str

class AdminLogin(BaseModel):
    email: EmailStr
    password: str

class AdminResponse(BaseModel):
    id: str
    email: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class LoginResponse(BaseModel):
    message: str
    admin: AdminResponse

# API Endpoints
@router.post("/register", response_model=AdminResponse, status_code=status.HTTP_201_CREATED)
def register_admin(admin: AdminCreate, db: Session = Depends(get_db)):
    """
    Register a new admin user
    """
    # Check if email already exists
    existing_admin = db.query(Admin).filter(Admin.email == admin.email).first()
    if existing_admin:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Create new admin
    new_admin = Admin(
        id=generate_admin_id(),
        email=admin.email,
        password=admin.password
    )
    
    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)
    
    return new_admin

@router.post("/login", response_model=LoginResponse)
def login_admin(credentials: AdminLogin, db: Session = Depends(get_db)):
    """
    Login admin user
    """
    # Find admin by email
    admin = db.query(Admin).filter(Admin.email == credentials.email).first()
    
    if not admin:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    
    # Verify password
    if credentials.password != admin.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    
    return {
        "message": "Login successful",
        "admin": admin
    }

@router.get("/get-by/{admin_id}", response_model=AdminResponse)
def get_admin_by_id(admin_id: str, db: Session = Depends(get_db)):
    """
    Get admin by ID
    """
    admin = db.query(Admin).filter(Admin.id == admin_id).first()
    
    if not admin:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Admin not found"
        )
    
    return admin

@router.get("/get-all", response_model=List[AdminResponse])
def get_all_admins(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Get all admins with pagination
    """
    admins = db.query(Admin).offset(skip).limit(limit).all()
    return admins
