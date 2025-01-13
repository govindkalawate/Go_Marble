import os
import openai
import asyncio
import random
from playwright.async_api import async_playwright
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import re

load_dotenv()

class ReviewScraper:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    async def get_dynamic_selectors(self, html_content):
        """Request dynamic selectors from OpenAI based on the HTML content"""
        max_retries = 5
        base_wait_time = 2  
        max_length = 10000 
        if len(html_content) > max_length:
            html_content = html_content[:max_length]

        for attempt in range(max_retries):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {
                            "role": "user",
                            "content": f"Provide CSS selectors for review elements (like review body, reviewer, rating) based on the following HTML content:\n\n{html_content}"
                        }
                    ]
                )
                await asyncio.sleep(5)  

                # Ensure the response contains only valid selectors
                selectors = response['choices'][0]['message']['content'].strip().splitlines()

                # Clean up unwanted characters and filter invalid selectors
                valid_selectors = [s.strip() for s in selectors if "{" not in s and ";" not in s and ":" not in s]
                valid_selectors = [s.lstrip('0123456789.').strip() for s in valid_selectors]

                # Filter out style and script selectors
                valid_selectors = [s for s in valid_selectors if "style" not in s and "script" not in s]

                if not valid_selectors:
                    print("No valid CSS selectors found in the response.")
                    return None

                return valid_selectors

            except openai.error.RateLimitError:
                wait_time = base_wait_time * (2 ** attempt) + random.uniform(0, 1)
                print(f"Rate limit exceeded. Waiting for {wait_time:.2f} seconds before retrying...")
                await asyncio.sleep(wait_time)
            except Exception as e:
                print(f"Error getting selectors: {e}")
                return None

        print("Max retries reached. Unable to get selectors.")
        return None

    async def handle_pagination(self, page):
        """Handles pagination, supporting both next button and infinite scroll"""
        pagination_buttons = await page.query_selector_all('a, button')
        for button in pagination_buttons:
            text = await button.inner_text()
            if 'next' in text.lower() or 'load more' in text.lower():
                await button.click()
                await page.wait_for_timeout(2000)  # wait for the content to load
                return True

        try:
            await page.evaluate("""
                window.scrollTo(0, document.body.scrollHeight);
                """)
            await page.wait_for_timeout(2000)  # wait for content to load
            return True
        except Exception as e:
            print(f"Error handling infinite scroll: {e}")
            return False

    async def extract_review_data(self, element):
        """Extracts various review data from a given element."""
        review_data = {}

        # Extract the body of the review
        body = await element.query_selector('p') or await element.query_selector('span')
        review_data['body'] = await body.inner_text() if body else "No review text"

        # Extract the title of the review (if present)
        title = await element.query_selector('h3') or await element.query_selector('strong')
        review_data['title'] = await title.inner_text() if title else "N/A"

        # Extract rating (numeric or stars)
        rating = await element.query_selector('.rating') or await element.query_selector('.star-rating')
        if rating:
            rating_text = await rating.inner_text()
            numeric_rating = re.search(r'\d+', rating_text)  # Match numeric rating
            review_data['rating'] = int(numeric_rating.group()) if numeric_rating else None
        else:
            review_data['rating'] = None


        reviewer = await element.query_selector('.reviewer') or await element.query_selector('.author')
        review_data['reviewer'] = await reviewer.inner_text() if reviewer else "Anonymous"

        author_info = await element.query_selector('.author-info')
        review_data['author_info'] = await author_info.inner_text() if author_info else "No additional info"

        return review_data

    async def scrape_reviews(self, url, max_pages=5):
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()
            await page.goto(url)

            reviews = []
            page_count = 0
            while page_count < max_pages:
                html_content = await page.content()
                soup = BeautifulSoup(html_content, 'html.parser')
                relevant_html = str(soup)

                selectors = await self.get_dynamic_selectors(relevant_html)

                if selectors is None:
                    print("No selectors returned. Trying default structure selectors.")
                    selectors = ['.review', '.a-review', '.review-text-content', '.review-body']  

                review_found = False  

                for selector in selectors:
                    print(f"Attempting to query with selector: {selector}")
                    try:
                        review_elements = await page.query_selector_all(selector.strip())
                        if review_elements:
                            review_found = True  # Mark as reviews found
                            for element in review_elements:
                                review = await self.extract_review_data(element)
                                reviews.append(review)
                    except Exception as e:
                        print(f"Error querying selector '{selector}': {e}")
                        continue

                if not review_found:
                    print("No reviews found with the selected selectors.")

                
                if not await self.handle_pagination(page):
                    break  

                page_count += 1

            await browser.close()
            return reviews


async def main():
    url = "https://2717recovery.com/products/recovery-cream"  
    scraper = ReviewScraper()
    reviews = await scraper.scrape_reviews(url)
    print(reviews)


if __name__ == "__main__":
    asyncio.run(main())
