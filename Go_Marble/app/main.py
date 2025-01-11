from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from .scraper import ReviewScraper  
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
scraper = ReviewScraper()

class Review(BaseModel):
    title: str
    body: str
    rating: int
    reviewer: str

class ReviewResponse(BaseModel):
    reviews_count: int
    reviews: List[Review]

@app.get("/api/reviews", response_model=ReviewResponse)
async def get_reviews(url: str, max_pages: int = 5):
    """
    API endpoint to get reviews from a product page.

    Args:
        url (str): The URL of the product page to scrape.
        max_pages (int): The maximum number of pages to scrape.

    Returns:
        ReviewResponse: A response containing the count and list of reviews.
    """
    try:
        all_reviews = await scraper.scrape_reviews(url, max_pages)

        if not all_reviews:
            raise HTTPException(status_code=404, detail="No reviews found")

        return ReviewResponse(reviews_count=len(all_reviews), reviews=all_reviews)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
