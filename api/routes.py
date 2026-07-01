from fastapi import APIRouter

from agent.portfolio_agent import PortfolioAgent
from api.schemas import ChatRequest, ChatResponse

router = APIRouter()

agent = PortfolioAgent()


@router.get("/")
def root():
    return {
        "message": "Welcome to Portfolio AI Agent"
    }


@router.get("/health")
def health():
    return {
        "status": "healthy"
    }


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    answer = agent.chat(request.question)

    return ChatResponse(answer=answer)