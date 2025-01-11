FROM python:3.9-slim

# Install necessary system dependencies
RUN apt-get update && apt-get install -y \
    libx11-xcb1 \
    libxkbcommon0 \
    libxcomposite1 \
    libxrandr2 \
    libxi6 \
    libasound2 \
    libatk1.0-0 \
    libnss3 \
    libxdamage1 \
    libgtk-3-0 \
    libdrm2 \
    libgbm1 \
    wget \
    curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set up a working directory
WORKDIR /app

# Copy project files
COPY . /app

# Upgrade pip and install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers
RUN playwright install

# Expose the app's port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
