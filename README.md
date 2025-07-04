# Kafka-Based Real-Time Messaging System

A Kafka-powered real-time messaging system built with **Docker** and **Python**. This project establishes a robust messaging pipeline where messages are sent by a Kafka producer and received in real-time by a Kafka consumer. Ideal for demonstrating distributed, event-driven data flow.

## Overview

This system enables real-time communication between microservices using Kafka as the backbone. It leverages Docker for isolated, containerized deployment and uses the `kafka-python` library for interacting with Kafka from Python scripts.

## Technologies Used 

- Apache Kafka  
- Zookeeper  
- Docker & Docker Compose  
- Python 3.13.0
- kafka-python  

## Key Features

- Fully containerized environment using Docker Compose  
- Kafka and Zookeeper orchestration  
- Python-based producer sends real-time messages  
- Python-based consumer listens and displays incoming messages  
- Easily extendable for larger event-streaming architectures  

## How It Works

1. Kafka and Zookeeper are initialized using Docker Compose.
2. A Kafka topic (e.g., `real-time-messages`) is created inside the Kafka container.
3. The **producer script** sends a series of messages to the topic.
4. The **consumer script** listens to the topic and prints messages in real time.

## Project Working Screenshots


## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/KafkaBasedRealTimeMessagingSystem.git
cd KafkaBasedRealTimeMessagingSystem
