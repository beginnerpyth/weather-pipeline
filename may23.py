from sqlalchemy import text,MetaData,create_engine,Integer,String,Float,Table,Column
from sqlalchemy.orm import Session,declarative_base
import os
from dotenv import load_dotenv
load_dotenv()
meta=MetaData()
engine=create_engine(os.getenv("sava"))
conn=engine.connect()

papa=Table("user",meta,Column("name" ,String(444)),Column("age" ,Integer))
sapa=Table("user_2",meta,Column("name",String(444)),Column("age",Integer))
papa.drop(engine)
sapa.drop(engine)
meta.create_all(engine)
vals=[{"name":"abhihek","age":22},{"name":"rmesh","age":25},{"name":"isikawa","age":19}]
vals2=[{"name":"nakamura","age":24},{"name":"seiya","age":19},{"name":"mac","age":20}]
inser_statement=papa.insert()#if we have to insert the datat more then one then we just need to make insert()
inser_statement2=sapa.insert()
sun=conn.execute(inser_statement,vals)#and then we ad the mutliple value i here
conn.commit()
conn.execute(inser_statement2,vals2)
conn.commit()
update_statement=papa.update().where(papa.c.name=="abhihek").values(age=24)
conn.execute(update_statement)
conn.commit()
join_statement=papa.join(sapa,papa.c.age==sapa.c.age)
select_statement=join_statement.select()#.with_only_columns(papa.c.name).where(papa.c.age >21)

#delete_statement=papa.delete().where(papa.c.age==24)
#conn.execute(delete_statement)
#conn.commit()
gun=conn.execute(select_statement)#just remember the execute cause if it is before the delete then it will
#show tables without deleting the vlues
for x in gun.fetchall():
    print(x)