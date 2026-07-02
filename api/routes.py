from fastapi import APIRouter, HTTPException

from api.schemas import ChatRequest, ChatResponse
from agent.portfolio_agent import PortfolioAgent

router = APIRouter()

agent = PortfolioAgent()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    try:

        response = agent.chat(request.message)

        return ChatResponse(
            success=response["success"],
            answer=response["answer"]
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

@router.get("/health")
def health():

    return {
        "status": "healthy"
    }