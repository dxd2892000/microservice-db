from sqlalchemy.orm import Session
from datetime import datetime

import models
import schemas

#crete new users
def creater_user(db: Session, user: schemas.UserCreate):
    new_user = models.User(
        name = user.name,
        password = user.password,
        createdTime = user.createdTime
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# update user
def update_user(db: Session, user_id: int, user_update: schemas.UserCreate):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        user.name = user_update.name
        user.password = user_update.password
        user.createdTime = user_update.createdTime or user.createdTime
        db.commit()
        db.refresh(user)
        return user
    return None


# delete user
def delete_user(db: Session, user_id: int):
    user = db.query(models.User).get(user_id)
    if user:
        db.query(models.Inference).filter(models.Inference.user_id == user_id).delete()
        db.delete(user)
        db.commit()
        return True
    return False

#get user by name
def get_user_by_name(db: Session, name: str):
    return db.query(models.User).filter(models.User.name == name).first()

# create a new inference
def create_inference(db: Session, inference: schemas.InferenceCreate):
    new_inference = models.Inference(
        name=inference.name,
        url=inference.url,
        result=inference.result,
        createdTime=inference.createdTime or datetime.now(),
        user_id=inference.user_id
    )
    db.add(new_inference)
    db.commit()
    db.refresh(new_inference)
    return new_inference

# update inference
def update_inference(db: Session, inference_id: int, inference_update: schemas.InferenceCreate):
    inference = db.query(models.Inference).filter(models.Inference.id == inference_id).first()
    if inference:
        inference.name = inference_update.name
        inference.url = inference_update.url
        inference.result = inference_update.result
        inference.createdTime = inference_update.createdTime or inference.createdTime
        inference.user_id = inference_update.user_id
        db.commit()
        db.refresh(inference)
        return inference
    return None


#delete inference by user
def delete_inference(db: Session, inference_id: int):
    inference = db.query(models.Inference).get(inference_id)
    if inference:
        db.delete(inference)
        db.commit()
        return True
    return False

#get inference by user
def get_inferences_by_user(db: Session, user_id: int):
    return db.query(models.Inference).filter(models.Inference.user_id == user_id).all()

#get inference by id
def get_inference_by_id(db: Session, inference_id: int):
    return db.query(models.Inference).filter(models.Inference.id == inference_id).first()