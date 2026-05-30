FROM python:3.11
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ['uvicorn','complicated_project:visual','--host','0.0.0.0','--port','8000']

