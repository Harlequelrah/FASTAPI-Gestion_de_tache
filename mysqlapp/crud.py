from sqlalchemy.orm import Session,aliased,selectinload
from sqlalchemy.sql import func
from . import models as ms
from sqlalchemy import text
from typing import List,Tuple
from datetime import date
from enum import Enum
from fastapi import  HTTPException,status,Depends
from mysqlapp.database import get_db





def get_task(id:int,db:Session=Depends(get_db)):
    task= db.query(ms.Task).filter(ms.Task.id==id).first()
    if task is None:
        raise HTTPException(status_code=404, detail='Tache non trouvé')
    else:return task
