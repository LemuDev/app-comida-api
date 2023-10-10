from apiflask import APIBlueprint
from src.config.db import engine

from .schemas.register import RegisterIn
from .schemas.login import LoginIn

from sqlmodel import Session, select
from .models import User
from .utils.user import create_user, create_token
from .utils.user import get_user_by_email

bp = APIBlueprint("auth", __name__, url_prefix="/api")

@bp.post("/register")
@bp.input(RegisterIn)
def register(json_data):
    email = json_data["email"]    
    user_by_email = get_user_by_email(email)
    
    
    if user_by_email is not None:
        return {
            "error": "This already exists"
        }, 400
    
    create = create_user(json_data)
    
    if not create:
        return{
            "error": "Error creating user. Try again"
        }, 400
        
        

    return{
        "access_token": create_token(email=email)
    }
    
@bp.post("/login")
@bp.input(LoginIn)
def login(json_data):
    email = json_data["email"]
    user_by_email = get_user_by_email(email)
    
    if user_by_email == None:
        return{
            "error": "Email or password Wrong"
        }, 400
    
    return{
        "access_token": create_token(email=email)
    }
    