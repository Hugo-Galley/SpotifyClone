import uvicorn
from config import setupLog
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.test import router


setupLog()

app = FastAPI()
app.include_router(router)
authorize_origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=authorize_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

if __name__ == "__main__":
    uvicorn.run("main:app",host="localhost", port=8000, reload=True)
