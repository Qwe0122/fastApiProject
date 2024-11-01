import uvicorn
from fastapi import FastAPI

from app.api.user_controller  import user_router


app = FastAPI()

app.include_router(user_router)

if __name__ == "__main__":
    uvicorn.run(app="main:app")
