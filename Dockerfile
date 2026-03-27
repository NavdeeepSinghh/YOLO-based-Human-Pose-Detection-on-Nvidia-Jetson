FROM python:3.9

WORKDIR /app

# ✅ Install system dependencies (THIS FIXES ERROR)
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0

# Copy project
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run app
CMD ["python", "test.py"]