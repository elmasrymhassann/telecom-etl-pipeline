FROM python:3.12-slim

# Set working directory

WORKDIR /app

# Copy requirements file

COPY requirements.txt .

# Install dependencies

RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files

COPY . .

# Run project

CMD ["python", "src/main.py"]