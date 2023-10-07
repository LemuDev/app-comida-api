from apiflask import APIBlueprint
from .schemas.restaurant import RestaurantsOut
from .models import Restaurant
from sqlmodel import Session, select
from src.config.db import engine
bp = APIBlueprint("restaurant", __name__, url_prefix= "/api")

@bp.get("/restaurant")
@bp.output(RestaurantsOut)
def restaurant_list():
    restaurants = []
    
    with Session(engine) as session:
        restaurants = session.exec(select(Restaurant)).all()
    
    response=  {
        "data":restaurants
    }
    
    
    return response