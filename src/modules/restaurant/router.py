from apiflask import APIBlueprint
from .schemas.restaurant import RestaurantsOut
from .models import Restaurant

from src.utils.paginator import Paginator
from src.schemas.paginator import PaginatorQuery

from src.modules.auth.utils.user import get_user_by_email

from flask_jwt_extended import jwt_required, get_jwt_identity

from .schemas.restaurant import RestaurantIn

from .utils.restaurant import create_restaurant_db, restaurant_by_name
import secrets

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


@bp.post("/restaurant")
@jwt_required()
@bp.doc(security='JWTAuth')
@bp.input(RestaurantIn, location='form_and_files')
def create_restaurant(form_and_files_data):
    email = get_jwt_identity()
    current_user = get_user_by_email(email)

    
    image_file = form_and_files_data['image'].mimetype
    
    if not current_user.is_admin:
        return {
            "msg": "Not valid token you must be Admin"
        }, 401
    
  
    
    if image_file != 'image/jpg' and image_file != 'image/jpeg' and image_file != 'image/webp' and image_file != 'image/png':
        return {
            'errors':{
                'image':'Invalid img file. must be .JPG, .JPEG, .PNG or .WEBP'
            }
        }      

        
    name = form_and_files_data['name']
    description = form_and_files_data['description']
    user_id = current_user.id
    image = form_and_files_data['image']
    

    create = create_restaurant_db(
        data={
            'name':name,
            'description':description,
        },
        user_id = user_id,
        image = image
    )
    
    if not create:
        return {
            'error': 'Error creating your Restaurant try again'
        }, 400
        
    
    return {
        'message': 'created successfully'
    }
