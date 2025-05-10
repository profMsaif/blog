# Use the official Python 3.12 slim image
FROM python:3.12-slim

# Set environment variables for Poetry
ENV POETRY_VERSION=2.1.2 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1

# Add Poetry to PATH
ENV PATH="$POETRY_HOME/bin:$PATH"

# Install system dependencies and Poetry
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    python3-dev \
    curl && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    apt-get remove -y curl && apt-get autoremove -y && apt-get clean && \
    rm -rf /var/lib/apt/lists/*
    
# Set the working directory
WORKDIR /app

# Copy only the dependency files to leverage Docker cache
COPY pyproject.toml poetry.lock* ./

# Install project dependencies without development packages
RUN poetry install --no-root --only main

# Copy the rest of the application code
COPY . .

# Expose the application port
EXPOSE 8000

# Define the default command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
