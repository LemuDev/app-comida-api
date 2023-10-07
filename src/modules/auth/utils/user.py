from sqlmodel import Session, select
from src.config.db import engine
from ..models import User
from flask_jwt_extended import create_access_token
import datetime

def create_user(data: dict):
    try:
        with Session(engine) as session:
            new_user = User(
                first_name = data["first_name"],
                last_name = data["last_name"],
                email = data["email"],
                password = data["password"]
            )        

            session.add(new_user)
            session.commit()

        return True
    except:
        return False

def get_user_by_email(email:str):
    with Session(engine) as session:
        results = session.exec(select(User).where(User.email == email)).one_or_none()
        
        return results




def create_token(email:str, days:int = 7):
    token = create_access_token(email, expires_delta=datetime.timedelta(days=days))
    return token