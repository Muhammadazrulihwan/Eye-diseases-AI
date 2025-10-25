from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from utils.pipeline import inference_pipeline
from utils.logger import logger
from models.labels import LABELS

app = FastAPI(
    title="Eye Disease Prediction API",
    description="API untuk deteksi penyakit mata berbasis CNN feature extraction + ML pipeline",
    version="1.0.0"
)

# ===== CORS MIDDLEWARE - PENTING! =====
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Untuk development, allow semua origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "status": "success",
        "message": "Eye Disease Prediction API is running."
    }

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "Eye Disease Prediction API"
    }

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        logger.info(f"Received file: {file.filename}")
        pred, confidence = inference_pipeline(image_bytes)
        
        if hasattr(pred, "item"):
            pred = pred.item()
        if hasattr(confidence, "item"):
            confidence = confidence.item()

        disease_name = LABELS[pred] if isinstance(pred, int) and pred < len(LABELS) else str(pred)

        return JSONResponse({
            "status": "success",
            "result": {
                "disease": disease_name,
                "confidence": round(float(confidence) * 100, 2) if confidence else None
            }
        })

    except Exception as e:
        logger.error(f"Prediction error: {e}")
        return JSONResponse(
            status_code=500,
            content={
                "status": "error",
                "message": str(e)
            }
        )