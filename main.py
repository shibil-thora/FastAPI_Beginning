from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from models import TestModel 
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI() 

# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api")
async def create_item(userInput: TestModel):
    return {
        "data": f"{userInput.name}",
    }

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message text was: {data}")
    except WebSocketDisconnect:
        print("Client disconnected")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
