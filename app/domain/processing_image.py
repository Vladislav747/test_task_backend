from fastapi import File
import base64
import cv2
import numpy as np


async def process_image(image: File) -> str:
    contents = await image.read()
    np_image = np.frombuffer(contents, np.uint8)
    cv_image = cv2.imdecode(np_image, cv2.IMREAD_COLOR)
    resized_image = cv2.resize(cv_image, (640, 640))
    normalized_image = cv2.normalize(resized_image, None, 0, 255, cv2.NORM_MINMAX)

    encoded_image = cv2.imencode(".jpg", normalized_image)[1].tobytes()
    return base64.b64encode(encoded_image).decode("utf-8")
