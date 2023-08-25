from typing import List, Optional
from fastapi import FastAPI, Query
from resolver import random_items

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "인덱스 주소임"} 

@app.get("/all/") 
async def all_movies():
    result = random_items()
    return {"message": result} 

@app.get("/genres/{genre}") # path param
async def genre_movies(genre: str):
    return {"message": f"genre: {genre}"} 

@app.get("/user-based/") # query param
async def user_based(params: Optional[List[str]] = Query(None)):
    return {"message": "user-based"} 

@app.get("/item-based/{item}")
async def item_based(item: int):
    return {"message": f"item-based: {item}"} 
