FROM python:3.12

# Install dependencies
RUN apt-get update && apt-get install -y \
    chromium chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Set display port (needed for headless)
ENV DISPLAY=:99

# Install Python dependencies
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy bot script
COPY bot.py .

# Run bot every 12 hours
CMD while true; do python bot.py; sleep 43200; done
