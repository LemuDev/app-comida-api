from sqlmodel import Session
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


def create_token(email:str, days:int = 7):
    token = create_access_token(email, expires_delta=datetime.timedelta(days=days))
    return token