from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from .config import settings
from .database import engine, Base
from .routes import mil_symbols

Base.metadata.create_all(bind=engine)

app = FastAPI(title="MIL Symbols Backend", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(level=getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO))
logger = logging.getLogger(__name__)

app.include_router(mil_symbols.router)

@app.get("/health")
def healthz():
    return {"status": "ok"}