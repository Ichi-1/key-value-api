"""Настройки FastAPI и запуск веб-сервера uvicorn"""
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.router import router as storage_api


app = FastAPI(
    docs_url="/",
    openapi_url="/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    storage_api,
    prefix='/api/v1/storage',
    tags=["Key-Value Storage"]
)


if __name__ == "__main__":

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8080,
        forwarded_allow_ips="*",
    )
