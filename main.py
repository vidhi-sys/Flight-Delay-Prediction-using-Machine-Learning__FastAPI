from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
import json
app=FastAPI()
#define route for endpoint
@app.get("/")#creating an object
#define method for endpoint
def hello():
    return {'message':'My flight Prediction System'}
#returns dictionary message hello world
@app.get('/about')
def about():
    return {'message':'This project implements a machine learning model to predict flight delays, inspired by recent disruptions in domestic aviation ....'}
#creating new view endpoint
#creatinf fxn to load data from json 
def load_data():
    with open('passenger.json', 'r') as f:
        data = json.load(f)
    return data

@app.get('/view')
def view():
    data=load_data()
    return data
#now we want to view specific flight data- slight modifications in the path(local host url)
@app.get('/passenger{passenger_id}')
def view_passenger(passenger_id:str= Path(..., description='ID of the passenger of flight in the DB', example='F001')):
    data=load_data()
    if passenger_id in data :
        return data[passenger_id]
    #normally returning  json with status code 200 is sucess we dont want that rather raise error with code 404
    raise HTTPException(status_code=404, detail='Passenger  not found')

#query paramater: view sorted data not chronologically
@app.get('/sort')
def sort(sort_by:str=Query(..., description='Sort on the basis of fligth delay, number or probablity'),order_by:str=Query('asc')):
    valid_fields=['flight_number','predicted_delay']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field select from {valid_fields}')
    
    if order_by not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order select between asc and desc')
    data=load_data()
    sort_order=True if order_by=='desc'else False
    sort_data= sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)
    return  sort_data
