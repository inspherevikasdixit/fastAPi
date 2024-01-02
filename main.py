from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app=FastAPI()

@app.get('/blog')

def index(limit=10,published:bool=True,sort:Optional[str]=None):
    #return published

    if published:
        return {'data':f'{limit} published blog from the Database'}
    else:
        return {'data':f'{limit}  blog from the Database'}

@app.get('/about')
def about():
    return{'data':'about page'}

@app.get('/blog/unpublished_blogs')
def unpublished_blogs():
    return {'data':'list of unpublished blogs'}

@app.get('/blog/{id}')
def show(id:int):
    return {'data':id}


@app.get('/blog/{id}/comments')
def comments(id,limit=10):
    return {'data':{'1','2'}}

class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]



@app.post('/blog')
def create_blog(request:Blog):
    return {'data':f'Create new blog with title name {request.title}'}



if __name__== "__main__":
    uvicorn.run(app,host="127.0.0.1",port=9000)