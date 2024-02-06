# Use the latest Ubuntu LTS as base image
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

# Set the working directory
WORKDIR /home/webServe

# Clone the repository
RUN git clone https://github.com/sud0gh0st-pwn/TG-Vendor-MiniApp.git

# Change Dir to project root
WORKDIR /home/webServe/TG-Vendor-MiniApp

# Switch to root to modify Nginx configuration
USER root

# Copy the Nginx configuration file and create symlink
COPY default.conf /etc/nginx/sites-available/default
RUN ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default
RUN rm /etc/nginx/sites-enabled/default

# Switch back to non-root user
USER webServe

# Change directory to the frontend directory
WORKDIR /home/webServe/TG-Vendor-MiniApp/frontend/telegram-webapp-front

# Install dependencies
RUN npm install

# Build your application if necessary
RUN npm install && \
    npm run build && \
    ls -l /home/webServe/TG-Vendor-MiniApp/frontend/telegram-webapp-front/dist


COPY ./telegram-webapp-front/dist /usr/share/nginx/html



# Expose ports for Nginx
EXPOSE 80 443

# Start Nginx in the foreground to keep the container running
CMD ["nginx", "-g", "daemon off;"]
