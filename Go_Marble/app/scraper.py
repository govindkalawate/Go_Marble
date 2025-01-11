import os
import openai
import asyncio
import random
from playwright.async_api import async_playwright
from dotenv import load_dotenv
from bs4 import BeautifulSoup


load_dotenv()

class ReviewScraper:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    async def get_dynamic_selectors(self, html_content):
        max_retries = 5
        base_wait_time = 2  
        max_length = 10000 
        if len(html_content) > max_length:
            html_content = html_content[:max_length]  # Truncate the content

        for attempt in range(max_retries):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {
                            "role": "user",
                            "content": f"Provide valid CSS selectors only (no explanations) for extracting reviews from the following HTML content:\n\n{html_content}"
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
                    print("No selectors returned. Trying default selectors.")
                    selectors = ['.review', '.a-review', '.review-text-content', '.review-body']  # Fallback selectors

                review_found = False  # Flag to check if reviews are found

                for selector in selectors:
                    print(f"Attempting to query with selector: {selector}")
                    try:
                        review_elements = await page.query_selector_all(selector.strip())
                        if review_elements:
                            review_found = True  # Mark as reviews found
                            for element in review_elements:
                                title = await element.query_selector('h3')  # Adjust based on actual structure
                                body = await element.query_selector('p')  # Adjust based on actual structure
                                rating = await element.query_selector('.rating')  # Adjust selector for rating
                                reviewer = await element.query_selector('.reviewer')  # Adjust selector for reviewer

                                if title and body:
                                    review = {
                                        'title': await title.inner_text(),
                                        'body': await body.inner_text(),
                                        'rating': int(await rating.inner_text()) if rating else None,  # Fallback if not found
                                        'reviewer': await reviewer.inner_text() if reviewer else "Anonymous"
                                    }
                                    reviews.append(review)
                    except Exception as e:
                        print(f"Error querying selector '{selector}': {e}")
                        continue

                if not review_found:
                    print("No reviews found with the selected selectors.")

                next_button = await page.query_selector('a.next')  # Adjust selector based on actual structure
                if next_button:
                    await next_button.click()
                    await page.wait_for_timeout(2000)
                    await asyncio.sleep(5)
                    page_count += 1
                else:
                    break

            await browser.close()
            return reviews
