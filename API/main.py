from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi import FastAPI, File, UploadFile, HTTPException
from typing import List
import db_alumnat
import alumnes

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AlumneModel(BaseModel):
    NomAlumne: str
    Cicle: str
    Curs: str
    Grup: str
    DescAula: str
#Activitat 1
@app.get("/alumnes/llista")
def read_alumnes():
    alumnes_data = db_alumnat.read()
    return alumnes.alumnes_schema(alumnes_data)
#Activitat 2
@app.get("/alumnes/list", response_model=List[AlumneModel])
def read_alumnes(orderby: str | None = None,  contain: str | None = None, skip: int = 0, limit: int | None = None ):
    alumnes_data = db_alumnat.read(orderby=orderby, contain=contain, skip=skip, limit=limit)
    if not alumnes_data:
        raise HTTPException(status_code=404, detail="No s'han trobat alumnes")
    return alumnes.alumnes_schema(alumnes_data)

#Activitat 3
@app.post("/alumne/loadAlumnes")
async def load_alumnes(file: UploadFile = File(...)):
    result = db_alumnat.alumnesCSV(file)   
    return result