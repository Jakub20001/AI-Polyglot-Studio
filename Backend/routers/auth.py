from fastapi import APIRouter

router = APIRouter()

@router.get("/auth/test")
def test():
    return {"message": "Auth router working"}
