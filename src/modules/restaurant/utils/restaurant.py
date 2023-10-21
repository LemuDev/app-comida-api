from src.config.db import engine

from sqlmodel import Session
from sqlmodel import select
from ..models import Restaurant
import os
import secrets
from werkzeug.utils import secure_filename
from decouple import config

def create_restaurant_db(data:dict, user_id:int, image):
    original_filename = image.filename
    filename, file_extension = os.path.splitext(original_filename)
    image_filename = secrets.token_hex(16) + file_extension 
    image.save(os.path.join('files/images', secure_filename(image_filename)))
    
    image_url = f'{config("BACKEND_URL")}/files/{image_filename}'
    
    try:
        with Session(engine) as session:
            restaurant = Restaurant(
                name = data['name'],
                description = data['description'],
                user_id=user_id,
                image_url= image_url
            )
            
            session.add(restaurant)
            session.commit()
        
        return True
    except:
        return False
    
    
def restaurant_by_name(name:str):
    with Session(engine) as session:
        results = session.exec(
            select(Restaurant).where(Restaurant.name == name)
        ).one_or_none()
        
        if results == None:
            return False
        else:
            return True
        
        
        