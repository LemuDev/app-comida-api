from apiflask import APIBlueprint


bp = APIBlueprint("auth", __name__)

@bp.post("/register")
def register():
    return{
        
    }