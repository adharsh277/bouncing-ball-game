# 🍉 Fruit Slice Game — Python, Docker & CI/CD Arcade Clone

This project brings a fun and simple arcade-style **Fruit Ninja-inspired game** to life using [Pygame](https://www.pygame.org/).  
You’ll slice flying fruits using your mouse, score points, and learn the **DevOps pipeline** along the way — from building with [Docker](https://www.docker.com/) to deploying and testing with [GitHub Actions](https://docs.github.com/en/actions).

Designed as a clean, CI/CD-ready mini-game to **level up your Python + DevOps portfolio**. ⚔️🍌

---

## 🚦 Tech Stack & Tools

[![Python](https://img.shields.io/badge/Python-Game%20Engine-yellow?logo=python)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/Pygame-2D%20Graphics-%2300A300?logo=pygame)](https://www.pygame.org/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-blue?logo=docker)](https://www.docker.com/)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-blue?logo=githubactions)](https://docs.github.com/en/actions)
[![Assets](https://img.shields.io/badge/Game%20Assets-Fruit%20Images-orange?logo=googlephotos)](https://freepngimg.com)
[![MIT License](https://img.shields.io/badge/License-MIT-green)](LICENSE)


---

## 🧠 What This Game Does

- 🥭 Fruits fly up from random positions with varying speed
- 🖱️ Click on fruits to slice them and earn points
- 🧮 Score shown live in top-right corner
- 🐳 Fully Dockerized setup for portability
- 🔁 CI/CD Pipeline with GitHub Actions builds Docker image on every push


## 🧩 Project Structure
bouncing-ball-game/
├── assets/ # Fruit images (apple.png, banana.png, etc.)
├── game.py # Main game logic
├── Dockerfile # Docker image setup
├── requirements.txt # Python dependencies
└── .github/
└── workflows/
└── docker.yml # CI/CD workflow

## 🖥️ Run Locally

### 1. Clone the Repo

```bash
git clone https://github.com/adharsh277/bouncing-ball-game.git
cd bouncing-ball-game

## Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
3. Play the Game!
bash
Copy
Edit
## python game.py
🐳 Run with Docker
✅ Requires X11 support (for GUI) if you're running in Docker

bash
Copy
Edit
docker build -t fruit-slice-game .
docker run -it fruit-slice-game
⚙️ CI/CD: GitHub Actions
Every time you push to the main branch, GitHub Actions will:

Checkout the repo

Build the Docker image

Run install steps (expandable for testing)

Config: .github/workflows/docker.yml





---
