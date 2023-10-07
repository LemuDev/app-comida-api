from apiflask import APIBlueprint

bp = APIBlueprint("restaurant", __name__, url_prefix= "/api")

@bp.get("/restaurant")
def restaurant_list():
    return{}