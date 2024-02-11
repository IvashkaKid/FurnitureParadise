from fastapi import FastAPI
import uvicorn

from routers.items import router as items_router
from products.views import router as products_router


app = FastAPI()

app.include_router(
    router=items_router,
    prefix='/items',
    tags=["Items"]
)
app.include_router(products_router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
