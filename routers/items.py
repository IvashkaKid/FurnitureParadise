from fastapi import APIRouter, Path
from pydantic import BaseModel

router = APIRouter()

@router.get("/")
def read_root():
    return [
        {
            "id": 1,
            "name": "first"
        }
    ]

@router.get("/{item_id}")
def read_item(item_id: int = Path(..., gt=1)):
    return {
        "item_id": {
            "id": item_id,
        },
        }