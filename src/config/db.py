from sqlmodel import Field, SQLModel, create_engine

# Models
from src.modules.auth.models import User


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


def migrate():
    SQLModel.metadata.create_all(engine)
    