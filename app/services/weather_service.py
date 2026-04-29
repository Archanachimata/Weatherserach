
import httpx

GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search"

WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


async def get_weather_by_city(city: str):
    """
    Fetch weather details for a city using Open-Meteo (No API key required)
    """

    async with httpx.AsyncClient(timeout=10.0) as client:

        geo_response = await client.get(
            GEOCODE_URL,
            params={"name": city, "count": 1}
        )

        geo_response.raise_for_status()
        geo_data = geo_response.json()

        if not geo_data.get("results"):
            return {"error": f"City '{city}' not found"}

        location = geo_data["results"][0]
        latitude = location["latitude"]
        longitude = location["longitude"]

        weather_response = await client.get(
            WEATHER_URL,
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current_weather": True
            }
        )

        weather_response.raise_for_status()
        weather_data = weather_response.json()

        current = weather_data.get("current_weather", {})

        return {
            "city": location["name"],
            "country": location.get("country"),
            "latitude": latitude,
            "longitude": longitude,
            "temperature_celsius": current.get("temperature"),
            "windspeed": current.get("windspeed"),
            "winddirection": current.get("winddirection"),
            "weathercode": current.get("weathercode"),
            "time": current.get("time")
        }
