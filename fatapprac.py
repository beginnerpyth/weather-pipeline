from fastapi import FastAPI,Path
from pydantic import BaseModel
from typing import Optional
med=FastAPI()

      
joji={1:{"song_name":"die_for_you","views":1222,"subscription":"one million"}}

class person(BaseModel):
    song_name:Optional[str]=None
    views:Optional[int]=None
    subscription:Optional[str]=None

class 更新(BaseModel):
      音楽の名前:Optional[str]=None
      回数:Optional[int]=None
      サブスクライブ:Optional[str]=None
      
@med.get('/引き出したい情報/')#query parameter no need to insert {}
def get_something(入れて:int):
    if 入れて not in joji:
          return "ここでは保存されていない"
    return joji[入れて]

@med.get("/getting/{id}")#pat parameter
def getting(id:int=Path(...,description=("if you dont insert then it will be set to none"),gt=1,lt=5)):#inside Path we cant insert the > < signs
        
    if id not in joji:
        return "ここでそのデータが保存されていない"
    return joji[id]
@med.post("/入力したい場合はこちらお願いします/")
def posting(num:int,追加:person):
      if num  in joji:
            return "以前から保存されています"
      joji[num]=追加
      return joji[num]
@med.put("/改めたい場合はこっちら/")
def updating(文字:更新,番号:int):
      
      if 番号 not in joji:
            return 'この番号は保存されていないから'
      if 文字.音楽の名前 != None:
         joji[番号].song_name = 文字.音楽の名前
        
      if 文字.回数 != None:
            joji[番号].views = 文字.回数
      if 文字.サブスクライブ != None:
           joji[番号].subscription=文字.サブスクライブ

      return joji[番号]
@med.delete("/消したい場合はこちらお願いします/")
def 削除(bum:int):
      if bum not in joji:
            return '保存されていない情報消すことができない'#return act as its stopppping point remember
      del joji[bum]
      return "データを削除しました" 



           
 
      
    



