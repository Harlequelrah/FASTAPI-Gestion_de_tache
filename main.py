from mysqlapp.database import Base,SessionLocal, engine
Base.metadata.create_all(bind=engine)
from   mysqlapp.database import get_db
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from datetime import date
import uvicorn
from routes.tache import app_tache
app = FastAPI()
app.include_router(app_tache)

if __name__=="__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)
