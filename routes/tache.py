from mysqlapp.crud import get_task
from mysqlapp import schemas as s,models as m
from sqlalchemy.orm import Session
from mysqlapp.database import get_db
from typing import List
from sqlalchemy.sql import func
from fastapi import APIRouter,Depends, FastAPI, HTTPException,Request,Form
app_tache=APIRouter(
    prefix='/taches',
    tags=['taches']
)

@app_tache.post("/taches/create-task",response_model=s.Task)
async def create_task(task:s.TaskCreate,db:Session=Depends(get_db)):
    db_task=m.Task(
    titre=task.titre,
    description=task.description,
    statut=task.statut ,
    priorite =task.priorite ,
    commentaire=task.commentaire ,
    date_echeance=task.date_echeance ,
    date_debut=task.date_debut ,
    date_fin=task.date_fin,
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@app_tache.get("taches/read-tasks",response_model=list[s.Task])
async def read_tasks(db:Session=Depends(get_db),skip:int=0,limit:int=None):
    return db.query(m.Task).order_by(m.Task.titre).offset(skip).limit(limit).all()

@app_tache.get("taches/read-tasks-by-id/{id}",response_model=s.Task)
async def read_tasks(id:str,db:Session=Depends(get_db)):
    return get_task(id,db)


@app_tache.get("/taches/get_count_task")
async def get_count_task(db:Session=Depends(get_db)):
    return db.query(func.count(m.Task.id)).scalar()

@app_tache.put("taches/update-task/{id}",response_model=s.Task)
async def update_task(task:s.TaskUpdate,id:int,db:Session=Depends(get_db)):
    db_task=get_task(id,db)
    if task.titre is not None:
        db_task.titre=task.titre
    if task.description is not None:
        db_task.description=task.description
    if task.statut is not None:
        db_task.statut=task.statut
    if task.priorite is not None:
        db_task.priorite=task.priorite
    if task.commentaire is not None:
        db_task.commentaire=task.commentaire
    if task.date_echeance is not None:
        db_task.date_echance=task.date_echeance
    if task.date_debut is not None:
        db_task.date_debut=task.date_debut
    if task.date_fin is not None:
        db_task.date_fin=task.date_fin
    db.commit()
    db.refresh(db_task)
    return db_task

@app_tache.delete("taches/delete-task/{id}",response_model=s.Task)
async def  delete_task(id:int,db:Session=Depends(get_db)):
    task=get_task(id,db)
    db.delete(task)
    db.commit()
    return task

