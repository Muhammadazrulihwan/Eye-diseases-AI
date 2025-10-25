import numpy as np
from PIL import Image
import io
from keras.applications.resnet50 import ResNet50, preprocess_input
from utils.config import IMAGE_SIZE
from utils.logger import logger

# Load ResNet50 
logger.info("Loading ResNet50 model for feature extraction...")
resnet_model = ResNet50(weights="imagenet", include_top=False, pooling="avg")

def prepare_image(image_bytes: bytes) -> np.ndarray:
    """Preprocess image bytes ke format input ResNet50"""
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    img = img.resize(IMAGE_SIZE)
    x = np.expand_dims(np.array(img), axis=0)
    x = preprocess_input(x)
    return x

def extract_features(img_array: np.ndarray) -> np.ndarray:
    """Ekstraksi fitur dari ResNet50"""
    features = resnet_model.predict(img_array)
    return features
