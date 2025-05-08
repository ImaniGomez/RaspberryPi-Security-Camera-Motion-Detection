# Raspberry Pi Security Camera with Motion Detection 
- This project is a security camera system with motion detection built using a Rapsberry Pi, a camera module and the Picamera2 library. It captures a live video feed and detects motion in real time by comparing frames and highlighting objects in motion. 

> This project was created for an NYU graduate course (Digital Signal Processing) that primarily focused on **audio processing and waveform analysis**, as an exploration into related real-time data processing techniques in video.

## Overview

The system captures consecutive frames from the Raspberry Pi Camera, processes them to identify motion, and displays bounding boxes around areas of significant change. It demonstrates real-time frame analysis using OpenCV and Python.

## Hardware Requirements
- Raspberry Pi 4 (or similar)
- Camera Module compatible with Picamera2
- Raspberry Pi 32-bit legacy OS (with libcamera support)
- Cables: Micro-HDMI to HDMI, USB-C power supply

## Libraries Used

- [`picamera2`](https://github.com/raspberrypi/picamera2): Interface with the Raspberry Pi camera module
- [`opencv-python`](https://pypi.org/project/opencv-python/): Image processing and motion detection
- `numpy`: Frame manipulation and array operations

### Author
Imani Gomez, NYU Tandon Graduate Student, 2025
Asmita Sonavane, NYU Tandon Graduate Student, 2025
  
