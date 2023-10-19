from src.config.db import engine

from sqlmodel import Session
from ..models import Restaurant


def create_restaurant(data:dict, user_id:int, image_url:str):
    with Session(engine) as session:
        restaurant = Restaurant(
            name = data['name'],
            description = data['description'],
            user_id=user_id,
            image_url=image_url
        )
        session.add(restaurant)
        session.commit()
