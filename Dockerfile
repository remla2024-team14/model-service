FROM python:3.11

WORKDIR /app

# Install required system dependencies
RUN apt-get -y update && apt-get install -y \
    libhdf5-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt separately to leverage Docker layer caching
COPY requirements.txt requirements.txt

# Install Python dependencies
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port on which your Flask app will run
EXPOSE 5001

CMD ["python", "app.py"]