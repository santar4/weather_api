# 🌦️ Weather App (Flask)

A production-style Flask web application that provides real-time weather data using the OpenWeather API.  
Includes authentication, database persistence, and secure form handling.

---

## 🚀 Features

- 🔐 User authentication (Signup / Login / Logout)
- 🌍 Search weather by city name
- 🌡 Real-time weather data via OpenWeather API
- 🧠 Session management (Flask-Login)
- 🛡 CSRF protection (Flask-WTF)
- 🗄 SQLite database with SQLAlchemy ORM
- ⚙️ Environment-based configuration (.env support)

---
**1. Home / Home page**  
![Home Page](screenshots/homepage.png)

**2. Weather page**  
![Weather page](screenshots/weatherpage.png)

**3. Sign up / Login form**  
![Sign up / Login form](screenshots/signup_login_page.png)


## 🛠 Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Jinja2](https://img.shields.io/badge/Jinja2-B41717?style=for-the-badge&logo=jinja&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-2E8B57?style=for-the-badge&logo=python&logoColor=white)
![dotenv](https://img.shields.io/badge/.env-000000?style=for-the-badge&logo=dotenv&logoColor=white)

---


---

## ⚙️ Installation

### 1. Clone repository

```bash
git clone https://github.com/your-username/weather-app.git
cd weather-app

python -m venv .venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt

SECRET_KEY=your_super_secret_key
API_KEY=your_openweather_api_key
Get API key here: https://openweathermap.org/api
python app.py