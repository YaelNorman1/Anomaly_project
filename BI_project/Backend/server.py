from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from Routes import anomalies_route, statistic_route, category_route


app = FastAPI()
app.include_router(anomalies_route.route)
app.include_router(statistic_route.route)
app.include_router(category_route.route)



origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return "Server On"

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)