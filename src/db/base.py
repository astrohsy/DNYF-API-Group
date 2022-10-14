# Standard library imports
import os

# Third party imports
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_host = os.getenv('DOCKER_DB_HOST', 'localhost')
SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://dbuser:dbuser@{db_host}:3306/dnyf-group-db'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
