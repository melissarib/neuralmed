from fastapi import FastAPI
from routers import person, patient

app = FastAPI()

app.include_router(person.router, prefix="/person", tags=["Person"])
app.include_router(patient.router, prefix="/patient", tags=["Patient"])