FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    python3-dev \
    libsdl2-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev \
    libsmpeg-dev libportmidi-dev libavformat-dev libswscale-dev \
    libfreetype6-dev && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "game.py"]
