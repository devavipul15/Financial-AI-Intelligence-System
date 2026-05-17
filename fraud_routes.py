from fastapi import APIRouter
from app.services.fraud_detection_service import predict_transaction

router = APIRouter()

@router.post("/predict")
def predict(data: dict):
    result = predict_transaction(data)
    return result