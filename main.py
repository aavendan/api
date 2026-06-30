from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "¡Hola, Fast API!"}

@app.get("/items/{item_id}")
def read_item(item_id):
   return {"item_id": item_id}