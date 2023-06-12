from fastapi import APIRouter, status, HTTPException

from fastapi.responses import JSONResponse
from random import choice
from schemas.image import ImageData

router = APIRouter(
    prefix="/ml",
    tags=['ml']
)


@router.post("/", status_code=status.HTTP_200_OK)
async def process_image(data: ImageData):
    if data.image:
        # Случайно выбираем отправлять или не отправлять результат
        if choice([True, False]):
            return {"res": {}}

        else:
            # Мы нашли машину
            top_left_x = 100
            top_left_y = 100
            width = 200
            height = 150
            confidence = 0.9
            label = 1

            return {"res": {top_left_x, top_left_y, width, height, confidence, label}}
    else:
        raise HTTPException(
            status_code=422,
            detail="No data.image provided",
        )
