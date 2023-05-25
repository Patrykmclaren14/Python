from fastapi import HTTPException, status
from blog.models import User
from ..hashing import Hash
from sqlalchemy.orm import Session
from blog import schemas


def create(db: Session, request: schemas.User):
    new_user = User(username=request.username,
                    email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user(id, db):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with the id {id} is not available')
    return user
