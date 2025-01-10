import os
import openai
from playwright.async_api import async_playwright
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class ReviewScraper:
    def __init__(self):
        # Set the OpenAI API key from environment variables
        openai.api_key = os.getenv("OPENAI_API_KEY")

    async def get_dynamic_selectors(self, html_content):
        """
        Use OpenAI's API to identify CSS selectors for reviews in the provided HTML content.

        Args:
            html_content (str): The HTML content of the product page.

        Returns:
            list: A list of CSS selectors for review elements.
        """
        response = await openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": f"Identify CSS selectors for reviews in the following HTML content:\n\n{html_content}"
                }
            ]
        )
        return response['choices'][0]['message']['content'].strip().splitlines()

    async def scrape_reviews(self, url):
        """
        Scrape reviews from the specified product page URL.

        Args:
            url (str): The URL of the product page to scrape.

        Returns:
            list: A list of dictionaries containing review data.
        """
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()
            await page.goto(url)

            reviews = []
            while True:
                # Get the page content
                html_content = await page.content()
                selectors = await self.get_dynamic_selectors(html_content)

                # Extract reviews based on the identified selectors
                for selector in selectors:
                    review_elements = await page.query_selector_all(selector.strip())
                    for element in review_elements:
                        title = await element.query_selector('h3')  # Adjust based on actual structure
                        body = await element.query_selector('p')  # Adjust based on actual structure
                        rating = await element.query_selector('.rating')  # Adjust based on actual structure
                        reviewer = await element.query_selector('.reviewer')  # Adjust based on actual structure

                        reviews.append({
                            "title": await title.inner_text() if title else "No Title",
                            "body": await body.inner_text() if body else "No Body",
                            "rating": int(await rating.inner_text()) if rating else 0,
                            "reviewer": await reviewer.inner_text() if reviewer else "Anonymous"
                        })

                # Check for a "Next" button or pagination link
                next_button = await page.query_selector('a.next')  # Adjust selector based on actual structure
                if next_button:
                    await next_button.click()
                    await page.wait_for_load_state('networkidle')  # Wait for the next page to load
                else:
                    break

            await browser.close()
            return reviews

# Example usage (if you want to run this script directly)
if __name__ == "__main__":
    import asyncio

    async def main():
        scraper = ReviewScraper()
        url = "https://2717recovery.com/products/recovery-cream"  # Replace with input URL if needed
        reviews = await scraper.scrape_reviews(url)
        print(reviews)

    asyncio.run(main())