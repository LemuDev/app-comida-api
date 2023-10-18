from apiflask import APIFlask
from decouple import config as env

from src.config.jwt import jwt
from src.config.cors import cors

from src.modules.auth.router import bp as auth_bp
from src.modules.restaurant.router import bp as restaurant_bp

app = APIFlask(__name__)

app.security_schemes = {
    'JWTAuth': {
        'type': 'http',
        'scheme': 'bearer',
        'bearerFormat': 'JWT',
    }
}


app.config["SECRET_KEY"] = env("SECRET_KEY")
app.config["JWT_SECRET_KEY"] = env("JWT_SECRET_KEY")

app.register_blueprint(auth_bp)
app.register_blueprint(restaurant_bp)


jwt.init_app(app)
cors.init_app(app)