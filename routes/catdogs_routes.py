import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

from fastapi import APIRouter, File, UploadFile
from schemas.catdog_schema import PredictionResponse
from configs.cat_dog_cfg import ModelConfig
from models.catdog_predictor import Predictor

router = APIRouter()
predictor = Predictor(model_name=ModelConfig.MODEL_NAME, model_weight=ModelConfig.MODEL_WEIGHT, device=ModelConfig.DEVICE)

@router.post("/predict")
async def predict(file_upload: UploadFile = File(...)):
    response = await predictor.predict(file_upload.file)
    return PredictionResponse(**response)

