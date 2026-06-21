from fastapi import FastAPI
from app.config import (
    LLM_PROVIDER
)
from app.api.agent import (
    router as agent_router
)
import logging

logging.basicConfig(level=logging.INFO)
logger  = logging.getLogger(__name__)


app = FastAPI(
    title="AgentFlow AI"
)

@app.on_event("startup")
async def startup():

    logger.info(
        "Using provider=%s",
        LLM_PROVIDER
    )


app.include_router(
    agent_router
)