from fastapi import APIRouter,Depends,HTTPException,status
from blog import models, schemas, token
from sqlalchemy.orm import Session
from blog.utils import get_db,verify_password

router = APIRouter()

@router.post('/login',response_model=schemas.Token)
def login(request : schemas.LoginScheme,db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Incorrect Password")

    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}