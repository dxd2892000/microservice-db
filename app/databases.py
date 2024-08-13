import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()  # Tải các biến môi trường từ tệp .env

# MySQL connection URL format

# DATABASE_USER = os.getenv('DATABASE_USER')
# DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
# DATABASE_HOST = os.getenv('DATABASE_HOST')
# DATABASE_NAME = os.getenv('DATABASE_NAME')

DATABASE_USER='root'
DATABASE_PASSWORD=''
DATABASE_HOST='localhost'
DATABASE_NAME='microservice'

SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}"
print(SQLALCHEMY_DATABASE_URL)
# Create the SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declare a base class for declarative class definitions
Base = declarative_base()