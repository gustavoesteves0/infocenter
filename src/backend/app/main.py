from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from api.routes import fetch_data
from api.routes import auth
from data.dependencies import Base, engine, SessionLocal

# Initialize FastAPI application
app = FastAPI()

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

Base = Base
engine = engine
SessionLocal = SessionLocal

# Middleware Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Pass database configuration to auth module
auth.engine = engine
auth.SessionLocal = SessionLocal
auth.Base = Base

app.include_router(fetch_data.router)
app.include_router(auth.router)

# Main entry point
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
