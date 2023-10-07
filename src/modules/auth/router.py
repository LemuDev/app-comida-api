from apiflask import APIBlueprint
from .schemas.register import RegisterIn

bp = APIBlueprint("auth", __name__)

@bp.post("/register")
@bp.input(RegisterIn)
def register(json_data):
    return{
        
    }