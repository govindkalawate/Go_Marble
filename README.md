
# GoMarble API

## Overview
The GoMarble API is a web service designed to extract product reviews from various e-commerce platforms using browser automation and OpenAI's language model for dynamic CSS identification. This API allows users to retrieve reviews from any product page, handling pagination and dynamic content effectively.

## Functionality
- **Ability to Extract Reviews**: The API can extract reviews from any product reviews page, including platforms like Shopify and Amazon.
- **Correct Handling of Pagination**: The API effectively manages pagination to retrieve all reviews, ensuring that no reviews are missed even if they span multiple pages.
- **Dynamic Content Handling**: The API is capable of handling dynamic content that may change based on user interactions or page loads.

## Technical Implementation
- **Dynamic CSS Identification**: The API utilizes Large Language Models (LLMs) to dynamically identify CSS selectors for reviews, allowing it to adapt to different website structures without hardcoding selectors.
- **Browser Automation Tools**: The API integrates browser automation tools, such as Playwright, to interact with web pages, scrape content, and navigate through pagination seamlessly.

## API Specification Compliance
- The API adheres to the provided API endpoint and response format, ensuring that it meets the expected standards for integration and usability.
- The API endpoints are designed to be intuitive and follow RESTful principles, making it easy for developers to use and integrate into their applications.
##  System Architecture :

![Untitled diagram-2025-01-10-171850](https://github.com/user-attachments/assets/d467eae8-99cd-42c6-90a9-7dcc30078e41)
                                                        System Architecture Diagram

**Description**: The System Architecture Diagram illustrates the overall architecture of the GoMarble API, showing how different components interact. It typically includes:

- **Client**: Represents the user interface or client application making requests to the API.
- **FastAPI Server**: The main server handling incoming requests.
- **Playwright**: The component responsible for web scraping.
- **OpenAI API**: The service used for dynamic CSS identification.

## System Workflow :
![mermaid-ai-diagram-2025-01-10-181913](https://github.com/user-attachments/assets/130a8e2d-8198-4e09-a0b3-e0adc32b26bc)
                                                          System Workflow Diagram

**Description**: The Workflow Diagram outlines the steps taken from receiving a request to returning the scraped reviews. It typically includes:

### Steps:
- **Receive Request**: The API receives a request from the client.
- **Validate Input**: Check if the input URL is valid.
- **Scrape Data**: Use Playwright to scrape the product page.
- **Process Data**: Extract relevant reviews and format them.
- **Return Response**: Send the response back to the client.

### Example Layout:
## Prerequisites

Before you begin, ensure you have the following installed on your system:

1. **Python 3.8 or Higher**: 
   - The GoMarble API is built using Python, so you need to have Python 3.8 or a later version installed. You can download it from the official Python website: [python.org](https://www.python.org/downloads/).

2. **Node.js**: 
   - Node.js is required for Playwright, which is used for browser automation. You can download it from the official Node.js website: [nodejs.org](https://nodejs.org/).

3. **OpenAI API Key**: 
   - You need an API key from OpenAI to use their language model for dynamic CSS identification. You can sign up and obtain an API key from the OpenAI website: [openai.com](https://openai.com/).

4. **Git**: 
   - Git is required to clone the repository. You can download it from the official Git website: [git-scm.com](https://git-scm.com/downloads).

5. **Playwright Browsers**: 
   - After installing Playwright, you will need to install the necessary browser binaries. This will be done as part of the installation steps.

6. **Virtual Environment (Optional but Recommended)**: 
   - It is recommended to use a virtual environment to manage your Python dependencies. You can create a virtual environment using `venv` or `virtualenv`. For example:
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows use `venv\Scripts\activate`
     ```

## Installation

### Steps to Install
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/govindkalawate/GoMarble.git
   cd GoMarble/app
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   Create a `.env` file in the app directory and add your OpenAI API key:
   ```plaintext
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Install Playwright Browsers**:
   ```bash
   playwright install
   ```

## Usage

### Running the API
To start the FastAPI server, run the following command:
```bash
uvicorn main:app --reload
```
The API will be available at `http://localhost:8000`.

### API Endpoints

#### Get Reviews
- **Endpoint**: `/api/reviews`
- **Method**: `GET`
- **Query Parameters**:
  - `url` (string): The URL of the product page to scrape.

- **Response**:
  - **200 OK**: Returns a JSON object containing the count of reviews and the list of reviews.
  - **500 Internal Server Error**: Returns an error message if an exception occurs.

- **Example Request**:
  ```bash
  curl "http://localhost:8000/api/reviews?url=https://2717recovery.com/products/recovery-cream"
  ```

- **Example Response**:
  ```json
  {
    "reviews_count": 5,
    "reviews": [
      {
        "title": "I love this stuff!",
        "body": "This product has changed my life for the better. Highly recommend!",
        "rating": 5
      },
      {
        "title": "Not what I expected",
        "body": "The product didn't work as advertised.",
        "rating": 2
      }
    ]
  }
  ```



   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   Create a `.env` file in the app directory and add your OpenAI API key:
   ```plaintext
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Install Playwright Browsers**:
   ```bash
   playwright install
   ```

## Usage

### Running the API
To start the FastAPI server, run the following command:
```bash
uvicorn main:app --reload
```
The API will be available at `http://localhost:8000`.

### API Endpoints

#### Get Reviews
- **Endpoint**: `/api/reviews`
- **Method**: `GET`
- **Query Parameters**:
  - `url` (string): The URL of the product page to scrape.

- **Response**:
  - **200 OK**: Returns a JSON object containing the count of reviews and the list of reviews.
  - **500 Internal Server Error**: Returns an error message if an exception occurs.

- **Example Request**:
  ```bash
  curl "http://localhost:8000/api/reviews?url=https://2717recovery.com/products/recovery-cream"
  ```

- **Example Response**:
  ```json
  {
    "reviews_count": 5,
    "reviews": [
      {
        "title": "I love this stuff!",
        "body": ```json
        "This product has changed my life for the better. Highly recommend!",
        "rating": 5
      },
      {
        "title": "Not what I expected",
        "body": "The product didn't work as advertised.",
        "rating": 2
      }
    ]
  }
  ```

## Conclusion
The GoMarble API provides a robust solution for extracting product reviews from various e-commerce platforms. With its dynamic CSS identification and browser automation capabilities, it simplifies the process of gathering reviews, making it a valuable tool for developers and businesses alike. If you have any questions or need further assistance, feel free to reach out!
