import os
import uvicorn
from fastapi import FastAPI
from starlette.responses import UJSONResponse

prefix = os.getenv('SCRIPT_PREFIX', '')
app = FastAPI()


@app.get(prefix + "/", response_class=UJSONResponse)
async def hello_world():
    """Hello world to check endpoint health"""
    return {"message": "hello world"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")