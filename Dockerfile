FROM python:3.11
WORKDIR /home/app
COPY . /home/app
RUN pip install -r requirements.txt
CMD ["python3","-m","uvicorn","complicated_project:visual","--host","0.0.0.0","--port","8000"] 
 