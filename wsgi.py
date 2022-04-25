import os

import uvicorn
from app.core import create_app
from uvicorn.config import logger
from app.db import database as db
from app.api.user.models import User
from app.api.auth.views import router
app = create_app()
app.include_router(router)


@app.on_event("startup")
def on_startup():
    db.init()


@app.get("/")
async def get_a():
    logger.info("aaaaaaaaaaaaaaaaaaaaabbbcDadwaf")
    return {"A": "a", "B": "b"}


if __name__ == "__main__":
    uvicorn.run("wsgi:app", host="0.0.0.0", port=int(os.environ.get("APP_PORT", 8000)), reload=True)
