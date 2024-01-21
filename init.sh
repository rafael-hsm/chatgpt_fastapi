#!/bin/bash

# Navigate to the source directory (adjust the path as needed)
cd /home/r4f43l/pessoal/chatgpt_fastapi

# Build the backend image
docker build -f Dockerfile.back -t chatgpt_backend .

# Build the frontend image
docker build -f Dockerfile.front -t chatgpt_frontend .

# Run the backend container
docker run -d -p 8000:8000 --name backend chatgpt_backend

# Run the frontend container
docker run -d -p 3000:3000 --name frontend chatgpt_frontend
