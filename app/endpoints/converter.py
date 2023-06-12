from fastapi import APIRouter, status, UploadFile, Depends, File

from crud.detection import save_detection
from domain.processing_image import process_image
from deps import get_db
import requests

from fastapi.responses import JSONResponse
from schemas.image import ImageData

router = APIRouter(
    prefix="/converter",
    tags=['converter']
)


@router.post("/", status_code=status.HTTP_200_OK)
async def send_file(image: UploadFile = File(...), db=Depends(get_db)):
    # Чтение и обработка изображения

    base64_image = await process_image(image)
    # Вызов микросервиса по обработке изображения
    ml_microservice_url = f"http://machine_image:8083/ml"

    data = ImageData(image=base64_image)
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    response = requests.post(ml_microservice_url, data=data.json(), headers=headers)
    formatted_response = response.json()
    if bool(formatted_response['res']):
        # Сохранение информации о детекции в базу данных
        save_detection(db, formatted_response['res'])

    return JSONResponse({"status": "success"})
