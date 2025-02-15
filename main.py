from typing import Optional
from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "Favorite Food", "content": "pizza is fav", "id": 2}]

@app.get("/")
def get_user():
    return {"message": "Hello Python"}

@app.get("/posts")
def get_post():
    return {"data": my_posts}


@app.post("/posts")
def create_posts(post: Post):
    print(post)
    print(post.model_dump())
    return {"data": "post"}