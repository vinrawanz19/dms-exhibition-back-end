from fastapi import FastAPI
from router.content import routerContent
from router.form import routerForm
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:59704",   # Replace with your frontend URL
    "http://localhost:8000",    # Replace with your backend URL
    "http://localhost"          # Add any other necessary origins
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# ROUTER
app.include_router(routerContent)
app.include_router(routerForm)

# UVICORN
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)

