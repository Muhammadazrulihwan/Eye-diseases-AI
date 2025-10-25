from utils.preprocessing import prepare_image, extract_features
from utils.model_loader import predict_from_features

def inference_pipeline(image_bytes: bytes):

    img_array = prepare_image(image_bytes)
    features = extract_features(img_array)
    pred, confidence = predict_from_features(features)
    return pred, confidence
