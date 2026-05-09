# Weather Pipeline 🌤️
# 天気データパイプライン

ETL pipeline that fetches live weather data and serves it via REST API.
リアルタイム天気データを取得しREST APIで提供するETLパイプライン

## Tech Stack
- Python
- FastAPI
- SQLAlchemy ORM
- MySQL
- Pandas

## Features
- Fetches live weather data from Open-Meteo API
- Stores data in MySQL database
- Exposes data via FastAPI REST endpoints
- Secure credentials with dotenv

## How to run / 実行方法
1. Clone repo
2. Create .env file with DATABASE_URL
3. pip install -r requirements.txt
4. python complicated_project.py
