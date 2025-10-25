import joblib
from utils.config import MODEL_PATH
from utils.logger import logger

_model_pipeline = None

def load_model():
    """Load model pipeline """
    global _model_pipeline
    if _model_pipeline is None:
        logger.info(f"Loading model pipeline from {MODEL_PATH}")
        _model_pipeline = joblib.load(MODEL_PATH)
    return _model_pipeline

def predict_from_features(features):
    """Prediksi penyakit mata berdasarkan fitur"""
    model = load_model()
    pred = model.predict(features)[0]
    confidence = None
    if hasattr(model, "predict_proba"):
        confidence = float(model.predict_proba(features).max())
    return pred, confidence
