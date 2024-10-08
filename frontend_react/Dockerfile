# Use an official Node runtime as the base image
FROM node:lts-slim

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json (if available)
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the frontend code
COPY . .

# Serve the app
CMD ["npm", "run", "dev"]
