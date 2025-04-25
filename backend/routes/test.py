from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def homePage():
    return {"Message" : "Bienvenue sur l'APi de Spotify"}