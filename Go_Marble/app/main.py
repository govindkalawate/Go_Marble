from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from scraper import ReviewScraper

# Initialize FastAPI application
app = FastAPI()
scraper = ReviewScraper()

class ReviewResponse(BaseModel):
    """
    Pydantic model for the response structure of the reviews API.
    """
    reviews_count: int
    reviews: list

@app.get("/api/reviews", response_model=ReviewResponse)
async def get_reviews(url: str):
    """
    API endpoint to get reviews from a product page.

    Args:
        url (str): The URL of the product page to scrape.

    Returns:
        ReviewResponse: A response containing the count and list of reviews.
    """
    try:
        reviews = await scraper.scrape_reviews(url)
        return {
            "reviews_count": len(reviews),
            "reviews": reviews
        }
    except Exception as e:
        # Raise an HTTP exception with a 500 status code if an error occurs
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    # Run the FastAPI application
    uvicorn.run(app, host="0.0.0.0", port=