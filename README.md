# Weather + Maps API Integration Project (FastAPI)

##  Overview
This project is a **FastAPI-based backend application** that demonstrates real-world third-party API integration. It allows users to search for any city and get live weather data along with geographical location details.

The project is designed using a modular architecture similar to production-level backend systems.

---

##  Features
-  Get real-time weather data by city name  
-  Convert city name into latitude & longitude  
-  Async API calls using httpx  
-  Clean service-based architecture  
-  Simple web UI for city search (optional)  

---

## Tech Stack
- FastAPI  
- Python  
- httpx (Async HTTP requests)  
- Jinja2 (HTML templates)  
- Open-Meteo API (Weather)  
- OpenStreetMap API (Geocoding)  

---

## 🚀 How It Works
1. User enters a city name  
2. System fetches latitude & longitude using Geocoding API  
3. Weather API returns live weather data  
4. Response is shown in JSON or UI format  

---

## 📁 Project Structure
app/
├── main.py
├── routes/
├── services/
├── templates/
requirements.txt
README.md


---

## 📌 API Endpoints
- `GET /` → Home page  
- `GET /weather/{city}` → Get weather by city  

Example:
/weather/Hyderabad

---

## Output Preview
<img width="683" height="743" alt="weatherSearch_UI" src="https://github.com/user-attachments/assets/73dd852f-b708-4c74-b335-74e7c6f0cfa6" />

When a user enters a city name, the system:
- Fetches location coordinates  
- Calls weather API  
- Returns formatted real-time weather data  

---

## Project Goal
This project demonstrates:
- Third-party API integration  
- Async backend development  
- Clean architecture design  
- Real-world API handling  

---

##  Future Improvements
- Payment gateway integration (Stripe/Razorpay)  
- Redis caching  
- JWT authentication  
- Docker deployment  
- React frontend  

---

## 👨‍💻 Author
Built as a backend portfolio project to showcase FastAPI + API integration skills.
