GoMarble API
Overview
The GoMarble API is a web service designed to extract product reviews from various e-commerce platforms using browser automation and OpenAI's language model for dynamic CSS identification. This API allows users to retrieve reviews from any product page, handling pagination and dynamic content effectively.
Features
Dynamic CSS Identification: Utilizes OpenAI's LLM to identify CSS selectors for reviews dynamically.
Pagination Handling: Automatically navigates through multiple pages of reviews to ensure complete data extraction.
Universal Compatibility: Designed to work with various product review pages.
Installation
Prerequisites
Python 3.8 or higher
Node.js (for Playwright)
An OpenAI API key
Steps to Install
Clone the Repository:
git clone https://github.com/govindkalawate/GoMarble.git
cd GoMarble/app
Install Dependencies:
pip install -r requirements.txt
Set Up Environment Variables:

Create a .env file in the app directory and add your OpenAI API key
OPENAI_API_KEY=your_openai_api_key_here
Install Playwright Browsers:
playwright install
Usage
Running the API
To start the FastAPI server, run the following command:
uvicorn main:app --reloadThe API will be available at http://localhost:8000.

API Endpoints
Get Reviews
Endpoint: /api/reviews

Method: GET

Query Parameters:

url (string): The URL of the product page to scrape.
Response:

200 OK: Returns a JSON object containing the count of reviews and the list of reviews.
500 Internal Server Error: Returns an error message if an exception occurs.

Example Request:

curl "http://localhost:8000/api/reviews?url=https://2717recovery.com/products/recovery-cream"
{
  "reviews_count": 5,
  "reviews": [
    {
      "title": "I love this stuff!",
      "body": "This product has changed my life.",
      "rating": 5,
      "reviewer": "Shawna Churchill"
    },
    {
      "title": "It’s amazing",
      "body": "I can't believe how well it works.",
      "rating": 5,
      "reviewer": "Tania Patterson"
    }
  ]
}

{
  "reviews_count": 5,
  "reviews": [
    {
      "title": "I love this stuff!",
      "body": "This product has changed my life.",
      "rating": 5,
      "reviewer": "Shawna Churchill"
    },
    {
      "title": "It’s amazing",
      "body": "I can't believe how well it works.",
      "rating": 5,
      "reviewer": "Tania Patterson"
    }
  ]
}
Diagrams
Workflow Diagram

Explanation of Diagrams
System Architecture Diagram: This diagram illustrates the overall architecture of the GoMarble API, showing how different components interact, including the FastAPI server, the scraper, and the OpenAI API.

Workflow Diagram: This diagram outlines the workflow of the API, detailing the steps taken from receiving a request to returning the scraped reviews.

Code Quality
The code is organized into two main files: main.py and scraper.py. Each file is structured to promote readability and maintainability. Key practices include:

Modular Design: The scraper logic is encapsulated in a separate class, making it reusable and easier to test.
Asynchronous Programming: The use of asynchronous functions allows for efficient handling of I/O-bound operations, such as web scraping and API calls.
Error Handling: The API includes error handling to manage exceptions gracefully and provide meaningful feedback to users.

Contribution
Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
OpenAI for providing the language model.
Playwright for the browser automation framework.
Sachin Yadhav sir for opportunity.


