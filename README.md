<h1 align="left">Kafka Based Real Time Messaging System</h1>

<p align="left">
  <strong>Backend • Distributed Systems • Event Streaming • Docker • Apache Kafka</strong>
</p>

<!-- Badges -->
<p align="left">
  <img src="https://img.shields.io/badge/Apache%20Kafka-231F20?style=for-the-badge&logo=apachekafka&logoColor=white" alt="Kafka">
  <img src="https://img.shields.io/badge/ZooKeeper-FF6F00?style=for-the-badge&logo=apache&logoColor=white" alt="Zookeeper">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/kafka--python-FFD43B?style=for-the-badge&logo=python&logoColor=black" alt="Kafka-Python">
</p>



## 📘 Overview

The **Kafka Based Real Time Messaging System** demonstrates a **distributed, event driven messaging pipeline** built with **Apache Kafka** and **Docker**. Messages are sent by a Python based Kafka producer and received by a consumer in real time simulating robust data flow between microservices or applications. This project provides a **hands on implementation** of asynchronous communication and event streaming fundamentals using Kafka in a fully containerized environment.



## 🚀 Features

- Real-time message streaming between producer and consumer  
- Fully containerized setup using **Docker Compose**  
- **Kafka** and **Zookeeper** orchestration in isolated containers  
- Lightweight **Python producer-consumer scripts** using `kafka python`  
- Scalable and modular for multi-service architectures  
- Extendable for analytics, monitoring, or IoT pipelines  



## 🧠 Technical Overview

| Component | Description |
|------------|-------------|
| **Core Technologies** | Apache Kafka, Zookeeper |
| **Programming Language** | Python 3.13 with kafka python |
| **Containerization** | Docker & Docker Compose |
| **Architecture Type** | Distributed Event-Driven Messaging |
| **Deployment** | Works locally or in cloud containers |



## ⚙️ Workflow

1. **Initialization:** Start Kafka and Zookeeper using Docker Compose.  
2. **Topic Creation:** Define a topic (e.g., `real-time-messages`) inside the Kafka container.  
3. **Producer:** Sends a stream of messages to the Kafka topic.  
4. **Consumer:** Listens to the topic and prints incoming messages in real time.  

This workflow simulates real-world microservice data flow and asynchronous communication.



## 📷 Project Working Screenshots

![Kafka Messaging Screenshot 1](https://github.com/user-attachments/assets/534fd9bb-65d1-4940-88f4-5b65b19b99bd)
![Kafka Messaging Screenshot 2](https://github.com/user-attachments/assets/3e73884c-898e-4994-9ccc-d9748e294df1)
![Kafka Messaging Screenshot 3](https://github.com/user-attachments/assets/82366f83-7b26-4e88-94ae-9c0162e7dae9)



## 🔮 Future Enhancements

- Integrate with **Apache Spark** or **Flink** for real-time analytics  
- Add **REST or WebSocket API** endpoints for external producers  
- Incorporate **PostgreSQL/InfluxDB** for message persistence  
- Deploy on **AWS** or **Google Cloud** with container orchestration  
- Implement **stream monitoring dashboard** using **Grafana**  



## 👨‍💻 Author

**Developed by [D Kumar](https://github.com/dkumar0501)** **[IIT Patna]**

---

<p align="center">
  <em>“Streaming data is the heartbeat of modern systems.”</em>
</p>
