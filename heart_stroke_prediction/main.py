from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()

class Features(BaseModel):
    age:int
    gender:int
    hypertension:int
    heart_disease:int
    ever_married:int
    work_type:int
    Residence:int
    avg_glucose_level:float
    bmi:float   
    smoking_status:str


@app.post('/prediction')
def fetch_stroke_prediction(features:Features):
    for item in features.model_dump().items():
        print('feature is ',item)
    new_observation = pd.DataFrame([features.model_dump()])
    model = joblib.load('stroke_prediction_model.pkl')
    predictions = model.predict(new_observation)
    print(f'predictions is {predictions}')
    return {
        "result":predictions.tolist()
    }