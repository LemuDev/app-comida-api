from apiflask import APIFlask
from decouple import config as env

from src.config.jwt import jwt

from src.modules.auth.router import bp as auth_bp

app = APIFlask(__name__)

app.config["SECRET_KEY"] = env("SECRET_KEY")


app.register_blueprint(auth_bp)


jwt.init_app(app)