from fastapi import FastAPI, WebSocket, Request
from models import TestModel 
from fastapi.middleware.cors import CORSMiddleware 
import time 
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


app = FastAPI() 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
) 

templates = Jinja2Templates(directory='templates')

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket): 
    print(websocket)
    await websocket.accept() 
    while True: 
        data = await websocket.receive_text() 
        print(data)
        await websocket.send_text(data)


@app.get("/", response_class=HTMLResponse)
def read_index(request: Request): 
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/api/schedule")
async def create_item(userInput: TestModel):
    return {
        "data": f"{userInput.name}",
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
