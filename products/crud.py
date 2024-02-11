from products.schemas import CreateProduct

def create_product(product_in: CreateProduct): 
    product = product_in.model_dump()
    return {
        "succes": True,
        "product": product,
    }