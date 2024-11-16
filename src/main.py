from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.router import router as router_crypto

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, Vercel!"}

app.include_router(router_crypto)

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
