from fastapi import FastAPI
import uvicorn

from endpoints.ml import router as ml_router

app = FastAPI()

app.include_router(ml_router, tags=["ml"])

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host='0.0.0.0',
        port=8083,
        reload=False,
        debug=True,
    )
