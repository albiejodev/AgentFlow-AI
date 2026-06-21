from fastapi import APIRouter

from app.services.agent_service import (
    AgentService
)

router = APIRouter(
    prefix="/agent",
    tags=["Agent"]
)


@router.get("/chat")
def chat(
    session_id:str,
    question: str
):

    return AgentService.run(
        session_id,
        question
    )