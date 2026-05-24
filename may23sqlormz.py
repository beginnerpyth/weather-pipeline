from sqlalchemy.orm import declarative_base,relationship,Session,sessionmaker
from sqlalchemy import Integer,String,Float,Column,Table,ForeignKey,MetaData,create_engine
import os
from dotenv import load_dotenv
load_dotenv()
base=declarative_base()
class Anime(base):
    __tablename__="cartoon"
    name=Column(String(444))
    episodes=Column(Integer)
    id=Column(Integer,primary_key=True)
    viewer=relationship("Viewers",back_populates="anime")

class Viewers(base):
    __tablename__="people"
    name=Column(String(444))
    age=Column(Integer)
    hair=Column(Integer,primary_key=True)
    human_id=Column(Integer,ForeignKey(Anime.id))
    anime=relationship('Anime',back_populates="viewer")  

engine=create_engine(os.getenv("sava"))
Viewers.__table__.drop(engine,checkfirst=True)
Anime.__table__.drop(engine,checkfirst=True)


base.metadata.create_all(engine)
Session=sessionmaker(bind=engine)
session=Session()


new_anime=Anime(name="naruto",episodes=1200)
session.add(new_anime)
session.flush()
new_viewers=Viewers(name="nepali",age=20,hair=1,human_id=new_anime.id)
session.add(new_viewers)
session.commit()
print(new_anime.name)
print(new_anime.episodes)
print(new_viewers.name)#its juts how class works its just throwed object name
print(new_viewers.anime.name)#it gives us naruto cause its parent class and also where Viewersforeignkey is faced toward Anime
print([x.name for x in new_anime.viewer]) 
bbc=session.query(Anime.name,Viewers.name).all()#so what we are doing is inserting the classs 
print(bbc)
ccc=session.query(Anime)
print([x.episodes for x in ccc])#so i just extracted the class and fetched it by one by one
