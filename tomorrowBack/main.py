from fastapi import FastAPI
from api.api_v1.api import router as api_router
# from mangum import Mangum
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*"
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "root!"}


app.include_router(api_router, prefix="/api/v1")
# handler = Mangum(app)
