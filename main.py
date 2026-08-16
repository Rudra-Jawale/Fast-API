from fastapi import FastAPI
from models import Product
from database import Session, engine
import database_models

app = FastAPI()

database_models.Base.metadata.create_all(bind=engine)


# Get: Read
@app.get("/")
def greet():
    return "Hello"

products = [
    Product(id= 1,name="Phone",description="Budget Phone",price=99,quantity=10),
    Product(id=2,name="Laptop",description="Gaming Laptop",price=999,quantity=6),
    Product(id=3,name="Laptop",description="Gaming Laptop",price=999,quantity=3),
    Product(id=4,name="Laptop",description="Gaming Laptop",price=999,quantity=4)

]


@app.get("/products")
def get_all_products():
    db = Session()
    return products

@app.get("/products/{id}")
def get_product_by_id(id:int):
    for product in products:
        if product.id == id:
            return product
    return "product not found"

# Post: Create
@app.post("/products")
def add_product(product: Product):
    products.append(product)
    return product


# Put: Update

@app.put("/products")
def update_product(id:int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product Added Successfully"
        
    return "Product not found"


# delete: delete
@app.delete("/products/")
def delete_product(id:int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product Deleted Successfully"
        
    return "Product not found"