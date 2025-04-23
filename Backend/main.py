from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.database import engine, Base # type: ignore
from backend.routers import ( # type: ignore
    auth,
    users,
    xp,
    dialogue,
    quiz,
    mentor
)
from backend.analytics import logger, metrics # type: ignore

Base.metadata.create_all(bind=engine) 

app = FastAPI(
    title="AI Polyglot Studio",
    description="AI language learning platform (quizzes, dialogues, AI mentor, XP system).",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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
def read_root():
    logger.log_event("Root endpoint hit.")
    return {"message": "Welcome  to AI Polyglot Studio!"}

@app.get("/metrics")
def get_metrics():
    return metrics.get_app.metrics()