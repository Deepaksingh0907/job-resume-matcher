from app.database import Base
from app.database import engine
from app.models import Analysis
from app.models import User


def create_tables():
    Base.metadata.create_all(
        bind=engine
    )


if __name__ == "__main__":
    create_tables()
    print("Database tables created successfully.")