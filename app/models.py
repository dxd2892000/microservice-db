from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.databases import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(100), unique=True)
    password = Column(String(100))
    createdTime = Column(DateTime)

    # Thiết lập mối quan hệ với Inference
    inferences = relationship("Inference", back_populates="user")

class Inference(Base):
    __tablename__ = 'inference'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(100), unique=True)
    url = Column(String(100))
    result = Column(String(100))
    createdTime = Column(DateTime)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)

    # Thiết lập mối quan hệ với User
    user = relationship("User", back_populates="inferences")