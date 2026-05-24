from sqlalchemy import create_engine,text
from sqlalchemy.orm import Session
import os
from   dotenv import load_dotenv
import pandas as pd
import numpy as np
from fastapi import FastAPI
import requests
load_dotenv()
love=FastAPI()
engine=create_engine(os.getenv('sava'))
data=requests.get('https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m,weather_code,pressure_msl,dew_point_2m,rain,showers,snowfall')
#decoding from json to dicitonary)



dic=data.json()
print(dic)
#decoding into dataframe
df=pd.DataFrame(dic)
print(df)
print(df.columns)
print(df.head())
print(df.index)
print(df[['latitude','longitude','elevation','timezone','hourly']])
lat=dic['latitude']
lon=dic['longitude']
ele=dic['elevation']
time=dic['timezone']

hour=df['hourly']
hour_time=df['hourly']['time']
df1=pd.DataFrame(dic['hourly'])

hour_tup=list(df1.itertuples())

session=Session(engine)
session.execute(text('DROP TABLE IF EXISTS AGAIN'))
session.execute(text('CREATE TABLE AGAIN(LAT INT,LON INT,ELE INT,TIME VARCHAR(444),HOURLY_TIME DATETIME)'))

session.execute(text('INSERT INTO AGAIN VALUES(:lat,:lon,:ele,:time,:htime)'),[{'lat':lat,'lon':lon,'ele':ele,'time':time,'htime':x.time}for x in hour_tup])








session.commit()




