# Stage 1: Build the application
FROM node:latest as builder

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy the rest of your app's source code from your host to your image filesystem.
COPY . .

# Build the application
RUN npm run build

# Stage 2: Setup the Nginx server
FROM ubuntu:latest

# Run updates and install necessary packages
RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y nginx sqlite3 curl python3-venv git

# Install Node.js via NVM
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
ENV NVM_DIR /root/.nvm
ENV NODE_VERSION 21.6.1
RUN . "$NVM_DIR/nvm.sh" && nvm install $NODE_VERSION && nvm use $NODE_VERSION && nvm alias default $NODE_VERSION

# Add NVM binaries to path
ENV PATH /root/.nvm/versions/node/v$NODE_VERSION/bin:$PATH

# Create a non-root user
RUN useradd -m webServe

# Copy the Nginx configuration file and create symlink
COPY default.conf /etc/nginx/sites-available/default
RUN ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default
RUN rm /etc/nginx/sites-enabled/default

# Copy the built files from the builder stage to Nginx's serve directory
COPY --from=builder /app/dist /usr/share/nginx/html

# Expose ports for Nginx
EXPOSE 80 443

# Start Nginx in the foreground to keep the container running
CMD ["nginx", "-g", "daemon off;"]
