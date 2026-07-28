from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello() :
	return {"message":"Hello World \u2764"}

@app.get("/about")
def about() :
	return {"message":"I am Debayan"}
	
