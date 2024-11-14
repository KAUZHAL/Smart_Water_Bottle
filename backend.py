from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
import uvicorn
import datetime

from plot import plot_to_bytes

app = FastAPI()

origins = [
    "http://localhost:5500",
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserData(BaseModel):
    waterIntake : float

@app.post('/user_data')
async def collect_user_data(user_data: UserData):
    print(user_data.waterIntake)
    return { "message": "success"}

@app.get('/graph')
async def plot_graph():
    with open('xydb.txt', 'r') as f:
        txt = f.read().split('\n')
        # return {"txt": txt.split('\n') }
        water_timestamps = eval(txt[0])
        water_drunk = eval(txt[1])
    return StreamingResponse(plot_to_bytes(water_timestamps, water_drunk), media_type="img/png")

def start_server():
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000,
    )

if __name__ == "__main__":
    start_server()