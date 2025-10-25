from pathlib import Path

# Base directory (root project)
BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "xgb_pipeline.pkl"
IMAGE_SIZE = (224, 224)
