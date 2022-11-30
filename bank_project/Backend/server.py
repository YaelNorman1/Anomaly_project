from fastapi import FastAPI
import uvicorn
from Routes import transactionsRouter
from Routes import authenticationRouter
from fastapi.middleware.cors import CORSMiddleware
from Models.Database.dbController import run_init_script as db_init

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(authenticationRouter.router)
app.include_router(transactionsRouter.router)

if __name__ == "__main__":
    db_init()
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
