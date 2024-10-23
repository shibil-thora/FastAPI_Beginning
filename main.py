from fastapi import FastAPI, HTTPException 
from models import TestModel
app = FastAPI() 


#assistant api testing...
@app.post("/api")
async def create_item(userInput: TestModel): 
    return {
        "data": f"{userInput.name}", 
    } 


if __name__ == "__main__":
    import uvicorn  
    uvicorn.run(app, host="0.0.0.0", port=8000)