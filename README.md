# 🍉 Interactive Fruit-Slicing Game — Python, Docker & CI/CD Pipeline Integration

This project originated as a simple bouncing ball animation built using Python and Pygame. It was later enhanced into an interactive fruit-slicing game where various fruits rise from the bottom of the screen, and the user earns points by slicing them through mouse clicks.
The goal was to transform a basic game prototype into a more engaging and visually interactive experience, while also incorporating modern DevOps practices. The project is fully containerized using Docker and includes a GitHub Actions workflow that automates the build process via continuous integration.
This serves as a portfolio-ready demonstration of combining **Python game development** with **CI/CD automation** and **Docker-based deployment**.

## 🚦 Tech Stack & Tools

[![Python](https://img.shields.io/badge/Python-Game%20Engine-yellow?logo=python)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/Pygame-2D%20Graphics-%2300A300?logo=pygame)](https://www.pygame.org/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-blue?logo=docker)](https://www.docker.com/)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-blue?logo=githubactions)](https://docs.github.com/en/actions)
[![Assets](https://img.shields.io/badge/Game%20Assets-Fruit%20Images-orange?logo=googlephotos)](https://freepngimg.com)
[![MIT License](https://img.shields.io/badge/License-MIT-green)](LICENSE)


---
🧩 Project Structure
python
Copy
Edit
fruit-slice-game/
├── assets/             # Fruit images (apple.png, banana.png, etc.)
├── game.py             # Main game logic
├── Dockerfile          # Docker image setup
├── requirements.txt    # Python dependencies
└── .github/
    └── workflows/
        └── docker.yml  # CI/CD workflow
🖥️ Run Locally
1. Clone the Repo
bash
Copy
Edit
git clone https://github.com/adharsh277/bouncing-ball-game.git
cd bouncing-ball-game
2. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
3. Play the Game
bash
Copy
Edit
python game.py
✅ A window will open where fruits fly up — slice them with your mouse!

🐳 Run with Docker
✅ Requires X11 support if running in Docker on Linux/macOS

bash
Copy
Edit
docker build -t fruit-slice-game .
docker run -it fruit-slice-game
⚙️ CI/CD: GitHub Actions
Every time you push to the main branch, GitHub Actions will:

✅ Checkout the repo

🐳 Build the Docker image

⚙️ Install requirements

🚀 (Expandable) Add testing or auto-deployment steps

Workflow config is located at:

bash
Copy
Edit
.github/workflows/docker.yml



---
