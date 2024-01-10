from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import settings

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(auth.router)

@app.get("/")
def read_items():
    return {"data": "Hello World"}