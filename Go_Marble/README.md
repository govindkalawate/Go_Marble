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
  
## Frontend UI
-  Simple Frontend User Interface that interacts with API.
  
##  System Architecture :

![Untitled diagram-2025-01-10-171850](https://github.com/user-attachments/assets/d467eae8-99cd-42c6-90a9-7dcc30078e41)
                                                       <p align="center">
   System Architecture Diagram
</p>

**Description**: The System Architecture Diagram illustrates the overall architecture of the GoMarble API, showing how different components interact. It typically includes:

- **Client**: Represents the user interface or client application making requests to the API.
- **FastAPI Server**: The main server handling incoming requests.
- **Playwright**: The component responsible for web scraping.
- **OpenAI API**: The service used for dynamic CSS identification.

## System Workflow :
![mermaid-ai-diagram-2025-01-10-181913](https://github.com/user-attachments/assets/130a8e2d-8198-4e09-a0b3-e0adc32b26bc)
                                                         <p align="center">
  System Workflow Diagram
</p>

**Description**: The Workflow Diagram outlines the steps taken from receiving a request to returning the scraped reviews. It typically includes:

### Steps:
- **Receive Request**: The API receives a request from the client.
- **Validate Input**: Check if the input URL is valid.
- **Scrape Data**: Use Playwright to scrape the product page.
- **Process Data**: Extract relevant reviews and format them.
- **Return Response**: Send the response back to the client.


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
  curl "http://localhost:8000/api/reviews?url=https://<input url>"
  ```
- **Example Response**:  
```json
{
  "reviews_count": 5,
  "reviews": [
    {
      "title": "I love this stuff!",
      "body": "",
      "rating": 5,
      "reviewer": "Shawna Churchill"
    },
    {
      "title": "It’s amazing",
      "body": "",
      "rating": 5,
      "reviewer": "Tania Patterson"
    },
    
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
  curl "http://localhost:8000/api/reviews?url=https://<input url>
  ```

- **OUTPUTS After Sucessful Implementation**:
 ```json
{
  "reviews_count": 5,
  "reviews": [
    {
      "title": "I love this stuff!",
      "body": "",
      "rating": 5,
      "reviewer": "Shawna Churchill"
    },
    {
      "title": "It’s amazing",
      "body": "",
      "rating": 5,
      "reviewer": "Tania Patterson"
    },
    {
      "title": "So far so good. Still in trial stage",
      "body": "",
      "rating": 4,
      "reviewer": "Francis Alvir"
    },
    {
      "title": "So far so good",
      "body": "",
      "rating": 4,
      "reviewer": "G.P."
    },
    {
      "title": "Game-Changer With a Pleasant Scent",
      "body": "I absolutely love this product! I’ve been using it before my workouts, and it’s been a total game-changer. One of my favorite things about it is that it doesn’t smell like medicine—it has such a pleasant scent! I recently let my business partner use it on her knee that’s been giving her trouble, and she loved it just as much as I do. It’s effective, and enjoyable to use. I’ve even been sharing it on my social media because I believe in it so much. Great job, 27:17 team—thank you for creating such an amazing product!",
      "rating": 5,
      "reviewer": "Melvaree Witherspoon"
    }
  ]
}
```
<div style="text-align: center;">
    <img width="800" alt="Screenshot 2025-01-11 at 12 54 51 AM" src="https://github.com/user-attachments/assets/2479676f-43c8-417d-a3c5-dc2063099ae3"/>
      <p align="center">
   Output Screenshot 1
</p>

<div style="text-align: center;">
    <img width="800" alt="Screenshot 2025-01-11 at 12 52 22 AM" src="https://github.com/user-attachments/assets/716ab712-5c02-4fbb-a033-0cc49e59cf30" />
     <p align="center">
   Output Screenshot 2
</p>

  ### Testing the Hosted API with Postman
  ## Hosted Api Link:
```
https://scraping-298313983231.asia-south1.run.app/
```
  

To test the hosted FastAPI application, follow these steps:

### Step 1: Open Postman

1. **Download and Install Postman** (if you haven't already):
   - Go to the [Postman website](https://www.postman.com/downloads/) and download the application for your operating system.
   - Install Postman by following the installation instructions.

2. **Open Postman**: Launch the Postman application.

### Step 2: Create a New Request

1. **Create a New Request**:
   - Click on the **"New"** button or the **"+"** tab to create a new request.

2. **Select Request Type**:
   - In the new request tab, select **GET** from the dropdown menu (this is typically the default).

### Step 3: Enter the Request URL

1. **Enter the URL**:
   - In the request URL field, enter the following endpoint:
     ```
     https://scraping-298313983231.asia-south1.run.app/api/reviews?url=https://<input url>
     ```

### Step 4: Set Up Headers (if needed)

1. **Add Headers** (if your API requires any specific headers):
   - Click on the **"Headers"** tab below the URL field.
   - If your API requires an API key or any other headers, add them here. For example:
     - Key: `Authorization`
     - Value: `Bearer your_api_key_here` (if applicable)

### Step 5: Send the Request

1. **Send the Request**:
   - Click the **"Send"** button to send the request to your FastAPI application.

### Step 6: View the Response

1. **Check the Response**:
   - After sending the request, you will see the response from your API in the lower section of Postman.
   - You can view the response body, status code, and headers.
   - If the request was successful, you should see the scraped reviews or any other data returned by your API.

### Step 7: Debugging (if needed)

1. **Check for Errors**:
   - If you receive an error response (e.g., 500 Internal Server Error), check the response body for any error messages that can help you debug the issue.
   - Ensure that the URL you are passing as a parameter is valid and accessible.

# Optimization Scope In Future

To enhance the performance and efficiency of the Flask application, the following optimizations can be implemented :

## 1. Redis for Caching

### Overview
Implementing Redis as a caching layer will help reduce the number of API calls made for frequently accessed data. By storing the results of API calls in Redis, we can serve cached responses for subsequent requests, significantly improving response times and reducing the load on external APIs.

### Benefits
- **Reduced Latency**: Cached data can be retrieved much faster than making a new API call.
- **Lower API Costs**: Fewer API calls can lead to reduced costs, especially if the API has usage limits or charges per request.
- **Improved Scalability**: By offloading repeated requests to Redis, the application can handle more concurrent users without overwhelming the server.

### Implementation Steps
- Set up a Redis server (either locally or using a managed service).
- Integrate Redis into the Flask application using a library like `Flask-Caching`.
- Implement caching logic to store and retrieve data from Redis based on specific keys.

## 2. Rate Limiting

### Overview
Implementing rate limiting will help manage the number of requests that users can make to the API within a specified time frame. This can prevent abuse, reduce server load, and ensure fair usage among all users.

### Benefits
- **Server Protection**: Rate limiting can help protect the server from being overwhelmed by too many requests in a short period.
- **Improved User Experience**: By controlling the rate of requests, we can ensure that all users have a fair chance to access the API without experiencing slowdowns.
- **Enhanced Security**: Rate limiting can help mitigate certain types of attacks, such as denial-of-service (DoS) attacks.

### Implementation Steps
- Use a library like `Flask-Limiter` to implement rate limiting in the Flask application.
- Define rate limits based on user roles or endpoints (e.g., 100 requests per hour for regular users).
- Monitor and log rate-limited requests to analyze usage patterns and adjust limits as necessary.

## Conclusion

By implementing Redis for caching and rate limiting, we can significantly enhance the performance, scalability, and security of the Flask application. These optimizations will lead to a better user experience and more efficient resource utilization.
## Code Quality

The code is organized into two main files: `main.py` and `scraper.py`. Each file is structured to promote readability and maintainability. Key practices include:

- **Modular Design**: The scraper logic is encapsulated in a separate class, making it reusable and easier to test.
- **Asynchronous Programming**: The use of asynchronous functions allows for efficient handling of I/O-bound operations, such as web scraping and API calls.
- **Error Handling**: The API includes error handling to manage exceptions gracefully and provide meaningful feedback to users.
  
### Files and Directories : 
<img width="221" alt="Screenshot 2025-01-11 at 7 09 28 PM" src="https://github.com/user-attachments/assets/a3c8142b-e1a6-40e2-afc7-edb8788040bd" />

### Description of Files and Directories

- **Go_Marble**: The root directory of project.
  
- **app/**: Directory containing the application code.
  - **main.py**: The entry point of the FastAPI application, where the API routes are defined.
  - **scraper.py**: The main script that contains the `ReviewScraper` class, which handles scraping and interacting with the OpenAI API.

- **.env**: A file to store environment variables, including your OpenAI API key.

- **requirements.txt**: A file to list the Python packages required for your project.

- **README.md**: A file to provide an overview of your project, installation instructions, and usage details.


## Contribution

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- OpenAI for providing the language model.
- Playwright for the browser automation framework.
- Sachin Yadhav Sir and Swapnil Bari Sir for the opportunity.

## Conclusion
The GoMarble API provides a robust solution for extracting product reviews from various e-commerce platforms. With its dynamic CSS identification and browser automation capabilities, it simplifies the process of gathering reviews, making it a valuable tool for developers and businesses alike. If you have any questions or need further assistance, feel free to reach out!


