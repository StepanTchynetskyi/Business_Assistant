import uvicorn
from app.core import create_app
from uvicorn.config import logger

app = create_app()


@app.get("/")
async def get_a():
    logger.info("aaaaaaaaaaaaaaaaaaaaa")
    return {"A": "a"}


if __name__ == "__main__":
    uvicorn.run("wsgi:app", host="0.0.0.0", port=8000, reload=True)
