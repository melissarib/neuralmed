from typing import List
from config import settings
from pydantic import BaseModel
from fastapi import APIRouter, HTTPException, Query

import requests
from requests.auth import HTTPBasicAuth

router = APIRouter()

@router.get("/find" , tags=["Patient"], summary="Find a patient")
def find_patient(
    q: str = Query(..., description="Search query to find a patient"),
    limit: int = Query(10, description="Maximum number of results to return")
):
    url = f'{settings.integration_url}/patient?limit={limit}&q={q}'
    
    response = requests.get(
        url, 
        auth=HTTPBasicAuth(settings.basic_auth_username, settings.basic_auth_password)
    )
    
    if response.status_code == 200:
        return response.json()
    else:
        try:
            error_message = response.json()
        except ValueError:
            error_message = response.text
        raise HTTPException(status_code=response.status_code, detail={
            "message": "Failed to fetch data",
            "details": error_message
        })
    

# class Name(BaseModel):
#     givenName: str
#     familyName: str

# class Address(BaseModel):
#     address1: str
#     cityVillage: str
#     country: str
#     postalCode: str

# class CreatePerson(BaseModel):
#     names: List[Name]
#     gender: str
#     birthdate: str
#     addresses: List[Address]


# @router.post("/create" , tags=["Person"], summary="Create a patient")
# def create_patient(patient: CreatePerson):
#     url = f'{settings.integration_url}/patient'
    
#     response = requests.post(
#         url, 
#         json=patient.model_dump(),
#         auth=HTTPBasicAuth(settings.basic_auth_username, settings.basic_auth_password)
#     )
    
#     if response.status_code == 201:
#         return response.json()
#     else:
#         try:
#             error_message = response.json()
#         except ValueError:
#             error_message = response.text
#         raise HTTPException(status_code=response.status_code, detail={
#             "message": "Failed to fetch data",
#             "details": error_message
#         })