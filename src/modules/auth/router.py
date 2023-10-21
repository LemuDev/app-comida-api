from apiflask import APIBlueprint

from .schemas.register import RegisterIn
from .schemas.login import LoginIn

from .utils.user import create_user, create_token
from .utils.user import get_user_by_email

from werkzeug.security import check_password_hash

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
    password = json_data["password"]
    user_by_email = get_user_by_email(email)
    
    if user_by_email == None:
        return{
            "error": "Email or password Wrong"
        }, 400
    
    if not check_password_hash(user_by_email.password, password):
        return{
            "error": "Email or password Wrong"
        }, 400
    

        
    return{
        "access_token": create_token(email=email)
    }
