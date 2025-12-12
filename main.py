from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Annotated, Literal, Optional
import json
import pickle

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()


# Pydantic Models
class FlightInput(BaseModel):
    flight_number: int


class Passenger(BaseModel):

    id: Annotated[str, Field(..., description='Passenger ID', examples=['F001'])]
    flight_number: Annotated[int, Field(..., description='Flight Number')]
    predicted_delay: Annotated[int, Field(..., description='0 -> No Delay, 1 -> Delay')]
    probability: Annotated[float, Field(..., ge=0, le=1, description='Probability of delay')]


class PassengerUpdate(BaseModel):
    flight_number: Optional[int] = None
    predicted_delay: Optional[int] = None
    probability: Optional[float] = None


# Load & Save JSON


def load_data():
    with open('passenger.json', 'r') as f:
        data = json.load(f)
    return data


def save_data(data):
    with open('passenger.json', 'w') as f:
        json.dump(data, f, indent=4)



# Basic Endpoints


@app.get("/")
def home():
    return {"message": "Flight Delay Prediction System API"}


@app.get("/about")
def about():
    return {"message": "API to manage flight prediction results (CRUD + sorting)"}



# VIEW all passengers


@app.get("/view")
def view_all():
    data = load_data()
    return data


# VIEW a specific passenger


@app.get("/passenger/{passenger_id}")
def view_passenger(passenger_id: str = Path(..., description="Passenger ID")):

    data = load_data()

    if passenger_id in data:
        return data[passenger_id]

    raise HTTPException(status_code=404, detail="Passenger not found")



# SORT passengers


@app.get("/sort")
def sort_passengers(
    sort_by: str = Query(..., description="Sort by: flight_number, predicted_delay, probability"),
    order: str = Query("asc", description="Sort in asc or desc order")
):

    valid_fields = ['flight_number', 'predicted_delay', 'probability']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid field. Choose from {valid_fields}")

    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Order must be asc or desc')

    data = load_data()

    reverse_order = True if order == 'desc' else False

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=reverse_order)

    return sorted_data


# CREATE new passenger


@app.post("/create")
def create_passenger(passenger: Passenger):

    data = load_data()

    if passenger.id in data:
        raise HTTPException(status_code=400, detail="Passenger already exists")

    data[passenger.id] = passenger.model_dump(exclude=['id'])

    save_data(data)

    return JSONResponse(status_code=201, content={"message": "Passenger created successfully"})



# UPDATE passenger


@app.put("/edit/{passenger_id}")
def update_passenger(passenger_id: str, passenger_update: PassengerUpdate):

    data = load_data()

    if passenger_id not in data:
        raise HTTPException(status_code=404, detail="Passenger not found")

    existing_passenger = data[passenger_id]

    updated_fields = passenger_update.model_dump(exclude_unset=True)

    for key, value in updated_fields.items():
        existing_passenger[key] = value

    data[passenger_id] = existing_passenger

    save_data(data)

    return JSONResponse(status_code=200, content={"message": "Passenger updated successfully"})



# DELETE passenger


@app.delete("/delete/{passenger_id}")
def delete_passenger(passenger_id: str):

    data = load_data()

    if passenger_id not in data:
        raise HTTPException(status_code=404, detail="Passenger not found")

    del data[passenger_id]

    save_data(data)

    return JSONResponse(status_code=200, content={"message": "Passenger deleted successfully"})
@app.post("/predict")
def predict_delay(data: FlightInput):

    # convert incoming data to model-friendly format
    X = [[data.flight_number]]  

   
    predicted_delay = int(model.predict(X)[0])
    probability = float(model.predict_proba(X)[0][1])

    return {
        "flight_number": data.flight_number,
        "predicted_delay": predicted_delay,
        "probability": round(probability, 4)
    }
