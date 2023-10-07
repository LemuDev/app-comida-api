from apiflask import APIBlueprint
from src.config.db import engine

from .schemas.register import RegisterIn

from sqlmodel import Session, select
from .models import User
from .utils.user import create_user, create_token


bp = APIBlueprint("auth", __name__)

@bp.post("/register")
@bp.input(RegisterIn)
def register(json_data):
    email = json_data["email"]    
    user_by_email = None
    
    with Session(engine) as session:
        results = session.exec(select(User).where(User.email == email)).one_or_none()
        
        user_by_email = results
        
        print(user_by_email)
    
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
        "access_token": create_token()
    }