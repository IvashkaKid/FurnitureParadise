from fastapi import APIRouter
from products.schemas import CreateProduct
from products import crud


router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/")
def create_product(product: CreateProduct):
    return crud.create_product(product_in=product)