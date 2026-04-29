
from fastapi import APIRouter
from app.services.weather_service import get_weather_by_city

router = APIRouter(prefix="/weather", tags=["Weather"])


@router.get("/{city}")
async def weather(city: str):
    """
    Example:
    /weather/Hyderabad
    """
    return await get_weather_by_city(city)

