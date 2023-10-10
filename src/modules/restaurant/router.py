from apiflask import APIBlueprint
from .schemas.restaurant import RestaurantsOut
from .models import Restaurant
from sqlmodel import Session, select
from src.config.db import engine
from src.utils.paginator import Paginator
from src.schemas.paginator import PaginatorQuery
bp = APIBlueprint("restaurant", __name__, url_prefix= "/api")

@bp.get("/restaurant")
@bp.output(RestaurantsOut)
@bp.input(PaginatorQuery, location="query")
def restaurant_list(query_data): 
    paginator = Paginator(model=Restaurant, page=query_data.get('page', 1), rows_per_page=query_data.get('rows_per_page', 10))
    restaurants = paginator.get_data()
    prev_page = paginator.prev_page()
    next_page = paginator.next_page()

    current_url = "http://127.0.0.1:8000/api/restaurant"
    

    response=  {
        "data":restaurants
    }
    
    if prev_page is not None:
        response["prev_page"] = f'{current_url}?page={prev_page}&rows_per_page={paginator.rows_per_page}'
    
    if next_page is not None:
        response["next_page"] =  f'{current_url}?page={next_page}&rows_per_page={paginator.rows_per_page}'
    
    
    
    return response