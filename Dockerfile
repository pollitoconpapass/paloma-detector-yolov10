# Use the official Python image as the base image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies for OpenCV and audio playback
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    ffmpeg \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements to the container
COPY requirements.txt .

# Upgrade pip, setuptools, and wheel to avoid build issues
RUN pip install --upgrade pip setuptools wheel

# Install all the dependencies
RUN pip install -r requirements.txt

# Clone the YOLOv10 repository and install it
RUN git clone https://github.com/THU-MIG/yolov10.git
WORKDIR /app/yolov10
RUN pip install .

# Copy the entire project into the container
WORKDIR /app
COPY . .

# Expose the port
EXPOSE 8087

# Run the application
CMD ["python3", "app.py"]
