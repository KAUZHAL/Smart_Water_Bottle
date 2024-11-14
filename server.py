from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:8080",
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
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
    pass