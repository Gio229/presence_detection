# Real-Time Presence Detection with YOLOv10X, OpenCV, and Kafka

This project implements a real-time **object detection system** using a webcam and **YOLOv10X**, publishing detection events to **Apache Kafka**. 

---

## 📦 Features

- Real-time object detection using YOLOv10X (`ultralytics`)
- Live webcam feed with bounding boxes using OpenCV
- Kafka integration: publish detection results as JSON messages
- Kafka monitoring interface via **Kafdrop**

---

## Quick start

```bash
git clone <repo_url>
cd presence_detection
pip install -r requirement.txt
docker compose up -d --build
make run
```



---

## Project Structure Overview
```
presence_detection/
├── src/
│ ├── main.py
│ ├── utils.py 
│ └── config.py
├── requirements.txt
├── dockerfile
├── docker-compose.yml
├── Makefile
└── README.md
```

---

## How it work ?
A message is publishe on the kafka broker for each state change. Wether personne are detected or not. When personne is detected, message is published at defined interval of time
