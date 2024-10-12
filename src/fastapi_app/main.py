import azure.functions as func

import fastapi

from fastapi_app.api.api import router as api_router

app = fastapi.FastAPI()

@app.get("/sample")
async def index():
    return {
        "info": "Try /hello/Shivani for parameterized route.",
    }


@app.get("/hello/{name}")
async def get_name(name: str):
    return {
        "name": name,
    }


app.include_router(api_router, prefix="/api")