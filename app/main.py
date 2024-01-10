from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from uuid import UUID

from app.repositories import ProductRepository
from app.schemas import ProductSchemaIn, ProductSchemaOut

from .config import settings

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post(
    "/v1/products",
    status_code=status.HTTP_201_CREATED,
    response_model=ProductSchemaOut,
)
def create_product(product_in: ProductSchemaIn) -> ProductSchemaOut:
    product_out = ProductRepository.create(product_in)
    return product_out


@app.get(
    "/v1/products/{product_id}",
    status_code=status.HTTP_200_OK,
    response_model=ProductSchemaOut,
)
def create_product(product_id: UUID) -> ProductSchemaOut:
    product_out = ProductRepository.get(product_id)
    return product_out