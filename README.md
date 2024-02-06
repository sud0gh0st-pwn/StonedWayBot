
# A Telegram MiniApp For Vendors

## Overview
This MiniApp is designed to help vendors manage their operations on Telegram. It features systems for content, order, client, channel, tracking, and touchdown management. 

> **Author:** @sud0gh0st  
> **Version:** 1.0  
> **Languages:** Python, Vue.js, Vuetify, HTML, CSS, JS, Sqlite

As a vendor, this MiniApp simplifies the management of various aspects of your business, enhancing efficiency and customer experience.

## Prerequisites

Before you begin, ensure you have Docker and Docker Compose installed on your VPS. These tools are essential for running the MiniApp in a containerized environment. For more information:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### On Your VPS (Linux suggested)
Required:
- Docker
- Docker-compose

```bash
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt update
sudo apt install docker-ce
sudo systemctl status docker
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
sudo usermod -aG docker ${USER}
su - ${USER}
groups
git clone https://github.com/sud0gh0st-pwn/StonedWayBot.git
cd StonedWayBot
```

Start the application with :
```bash
docker-compose up
```

Stop the application with :
```bash
docker-compose down
```

## Features

- [x] Content Managment System
> An admin only access pannel to manage channel content.
- [x] Order Managment System
> An admin only dashboard and cli system for orders.
- [x] Client Managment System
> Automaticaly create a client account for new users.
- [x] Channel Managment System
> Manage the channel menu and stock automaticaly
- [x] Tracking Managment System
> Tracking updates sent to client in TG
- [x] TouchDown Managment System
> Automoderator for the channel. Updates Tracking & TD Together
