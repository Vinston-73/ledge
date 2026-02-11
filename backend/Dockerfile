# Use smaller Node base image
FROM python:3.11-slim

WORKDIR /app

# Copy only package files first (for caching)
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy remaining backend files
COPY . .

# Expose backend port
EXPOSE 4000

# Load environment variables from .env automatically
CMD ["npm", "start"]
