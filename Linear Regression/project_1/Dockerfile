# STAGE 1: Build dependencies to optimize final image size
FROM python:3.9-slim as builder

WORKDIR /app

# Copy only the requirements file to leverage Docker cache
COPY requirements.txt .

# Build wheels for faster installation in the next stage
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

# STAGE 2: Final application image
FROM python:3.9-slim

WORKDIR /app

# Copy the pre-built wheels from the builder stage
COPY --from=builder /app/wheels /wheels

# Install dependencies from the wheels
RUN pip install --no-cache /wheels/*

# Copy the entire application code into the image
# This includes the api, frontend, and all other necessary files
COPY . .

# Expose port 8000 to allow external traffic
EXPOSE 8000

# Command to run the Uvicorn server
# The host 0.0.0.0 makes the app accessible from outside the container
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"] 