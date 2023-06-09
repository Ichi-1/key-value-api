"""Эндпоинты для записи и чтения данных из embedded key-value хранилища"""
from fastapi import Query
from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from .storage import storage


router = APIRouter(prefix="/json")


@router.post("/write/")
async def add_key_value_pair(request: dict) -> JSONResponse:
    """
    Добавить пару/пары ключ-значение в хранилище
    """
    if not request.items():
        return JSONResponse({'detail': 'Body is empty'}, status_code=400)

    try:
        for key, value in request.items():
            storage.set(key, value)

        return JSONResponse(
            content=jsonable_encoder(request),
            status_code=201
        )
    except TypeError as error:
        return JSONResponse(
            content={
                'detail': 'TypeError while adding key-value pair into storage',
                'error': f'{error}'
            },
            status_code=409
        )


@router.get("/read/all/")
def get_keys() -> JSONResponse:
    """
    Получить все данные хранилища
    """
    keys = storage.getall()

    if keys:
        db_content = {key: storage.get(key) for key in keys }

        return JSONResponse(
            content=jsonable_encoder(db_content),
            status_code=200
        )

    return JSONResponse(
        content={'detail': 'Storage is empty'},
        status_code=404
    )


@router.get("/read/")
def get_key_by_query(key: str = Query()) -> JSONResponse:
    """Получить значение по ключу"""
    
    value = storage.get(key)
    
    if value:
        return JSONResponse({'result': value}, status_code=200)
    return JSONResponse(
        content={'result':'No value found with requested key'},
        status_code=404
    )
