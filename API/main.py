from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import db_alumnat
import alumnes
from typing import List
from pydantic import BaseModel
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

@app.get("/alumnes/llista", response_model=List[AlumneModel])
def read_alumnes():
    alumnes_data = db_alumnat.read()
    return alumnes.alumnes_schema(alumnes_data)
