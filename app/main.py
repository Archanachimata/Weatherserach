
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from app.routes.weather import router as weather_router

app = FastAPI(
    title="Weather Search App",
    description="Search weather by city",
    version="1.0.0"
)

templates = Jinja2Templates(directory="app/templates")

app.include_router(weather_router)


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "weather": None
        }
    )


@app.get("/search")
async def search_weather(request: Request, city: str):
    from app.services.weather_service import get_weather_by_city

    weather_data = await get_weather_by_city(city)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "weather": weather_data
        }
    )

