# from fastapi import FastAPI,HTTPException
# from pydantic import BaseModel
# import pandas as pd
# import joblib
# import numpy as np

# app = FastAPI()

# try:
#     model = joblib.load("./app/model/best_lr_model.joblib")
# except FileNotFoundError:
#     raise Exception("Model is not found")

# # Load your scaler if you used one
# try:
#     scaler = joblib.load("scaler.joblib")  # Replace with your scaler file if applicable
#     scaling_used = True
# except FileNotFoundError:
#     scaling_used = False
#     scaler = None


# # Define the input data structure using Pydantic
# class InputData(BaseModel):
#     age: int
#     gender_Female: int
#     gender_Male:int
#     gender_Other:int
#     study_hours_per_day: float
#     social_media_hours: float
#     netflix_hours: float
#     part_time_job: str
#     attendance_percentage: float
#     sleep_hours: float
#     diet_quality: str
#     exercise_frequency: int
#     parental_education_level: str
#     internet_quality: str
#     mental_health_rating: int
#     extracurricular_participation: str

# @app.post("/predict")
# async def predict(data:InputData):
#     try:
#          # Convert input data to a pandas DataFrame
#         input_df = pd.DataFrame([data.dict()])

#          # Preprocess the input data
#         categorical_features = ['part_time_job', 'diet_quality', 'parental_education_level', 'internet_quality', 'extracurricular_participation']
#         input_df = pd.get_dummies(input_df, columns=categorical_features, dummy_na=False)

#         # Ensure all expected columns are present
#         expected_columns = list(model.feature_names_in_)
#         for col in expected_columns:
#             if col not in input_df.columns:
#                 input_df[col] = 0
#         input_df = input_df[expected_columns]

#         # Scale the data if scaling was used
#         if scaling_used and scaler is not None:
#             input_scaled = scaler.transform(input_df)
#             prediction = model.predict(input_scaled)[0]
#         else:
#             prediction = model.predict(input_df)[0]

#         return {"predicted_exam_score": prediction}

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# # Optional: Health check endpoint
# @app.get("/health")
# async def health_check():
#     return {"status": "OK"}
# /app/main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "OK"}