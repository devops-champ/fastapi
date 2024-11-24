from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_user():
    return {"message": "Hello World"}

@app.get("/posts")
def get_post():
    return {"data": "This is your post"}


@app.post("/createposts")
def create_posts():
    return {"message": "successfully created posts"}     