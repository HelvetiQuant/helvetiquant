
from fastapi import APIRouter
from backend.modules import (
    dynamic_token_selector,
    sentiment_collector,
    macro_event_processor
)

router = APIRouter(prefix="/api")

@router.get("/watchlist")
def get_watchlist():
    return dynamic_token_selector.get_top_tokens()

@router.get("/sentiment")
def get_sentiment():
    return sentiment_collector.get_social_sentiment()

@router.get("/macro-news")
def get_macro_news():
    return macro_event_processor.get_macro_events()

@router.get("/status")
def get_status():
    return {"message": "HelvetiQuant API attiva - 3 token in monitoraggio"}
