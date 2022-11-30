import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import actor


# def setting_middleware(app):
#     app.add_middleware(
#         CORSMiddleware,
#         allow_origins=origins,
#         allow_credentials=True,
#         allow_methods=["*"],
#         allow_headers=['*']
#             )

app = FastAPI(
    title="Heart Stoper Intro",
    description="This API was developed for Fast API Homework",
    version="0.0.1",
    terms_of_service="http://localhost:5000",
)
app.include_router(actor.router)

origins = [
    'http://127.0.0.1:5173',
    'http://127.0.0.1:8080',
    'http://127.0.0.1:8081',
    'http://127.0.0.1:5174'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=['*']
)

@app.get("/")
def root():
    return {"title": 'HELLO'}


if __name__ == "__main__":
    uvicorn.run("app:app", port=5000, reload=True)