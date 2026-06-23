from ultralytics import YOLO
from PIL import Image

MODELS = {
    "26x": YOLO("./models/26x-200.pt"),
    "26l": YOLO("./models/26l-200.pt"),
    "26m": YOLO("./models/26m-200.pt"),
    "11x": YOLO("./models/11x-200.pt"),
    "11l": YOLO("./models/11l-200.pt"),
    "11m": YOLO("./models/11m-200.pt"),
    "8x": YOLO("./models/8x-200.pt"),
    "8l": YOLO("./models/8l-200.pt"),
    "8m": YOLO("./models/8m-200.pt"),
    "26x-2": YOLO("./models/26x-big.pt")
}

def process(files, model_name="26x"):
    images = [Image.open(file) for file in files]

    model = MODELS.get(model_name, MODELS["26x"])

    results = model.predict(
        source=images,
        conf=0.15,
        imgsz=2048,
        verbose=False,
        max_det=10_000
    )

    return results