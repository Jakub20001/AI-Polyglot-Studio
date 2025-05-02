from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv # type: ignore
import os 

from database import engine, Base 
from routers import  auth, users, xp, dialogue, quiz, mentor
from analytics import logger, metrics 

load_dotenv()

Base.metadata.create_all(bind=engine) 

app = FastAPI(title="AI Polyglot Studio")

origins = os.getenv("ALLOWED_ORIGINS", "*").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(xp.router)
app.include_router(dialogue.router)
app.include_router(quiz.router)
app.include_router(mentor.router)

@app.get("/")
def root():
    return {"message": "Welcome  to AI Polyglot Studio!"}

@app.get("/health", tags=["system"])
def health_check():
    return {"status": "ok"}

@app.on_event("startup")
def startup_event():
    print("🚀 App started")
    
@app.on_event("shutdown")
def shutdown_event():
    print("👋 App shutting down")

@app.get("/metrics")
def get_metrics():
    return metrics.get_app.metrics()
