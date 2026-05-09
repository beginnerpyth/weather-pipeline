from sqlalchemy.orm import declarative_base,sessionmaker,relationship
from sqlalchemy import Integer,String,Float,MetaData,create_engine,Column,ForeignKey
import os
from dotenv import load_dotenv
load_dotenv()

base=declarative_base()
engine=create_engine(os.getenv("baba"))
class gaga(base):
    __tablename__= "sala"
    name=Column(String(666))
    age=Column(Integer)
    value=Column(Integer)
    id=Column(Integer,primary_key=True)
    kos=relationship("baba",back_populates="mos")

class baba(base):
    __tablename__="haha"
    name=Column(String(555))
    age=Column(Integer)
    value=Column(Integer)
    owner_id=Column(Integer,primary_key=True)
    id=Column(Integer,ForeignKey(gaga.id))
    mos=relationship("gaga",back_populates="kos")

base.metadata.create_all(engine)
Session=sessionmaker(bind=engine)
session=Session()

object1=gaga(name="tsukamoto",age=33,value=2200)
session.add(object1)
session.flush()
session.commit()

object2=baba(name="sakamoto",age=22,value=4400,owner_id=object1.id,id=object1.id)
session.add(object2)
session.commit()
print([x.name for x in object1.kos])
print(object2.mos.name)
    