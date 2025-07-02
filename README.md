#  Raspberry Pi Dashcam – IoT-Based Smart Surveillance & Crash Detection System

This project implements a smart, Iot based, low-cost **Dashcam system using Raspberry Pi**. It continuously records video, detects crashes using a vibration sensor (SW-420), and sends alert emails with video footage upon impact. Designed for vehicles, this solution is ideal for personal use, fleet monitoring, or DIY IoT setups.

---

## 🎯 Project Objective

Build a complete Iot based Raspberry Pi-based dashcam system that continuously records video, detects vibrations (accidents), and automatically alerts the user via email with a timestamp and video attachment.

---

## 🛠️ Features Implemented

-  **Continuous Video Recording** (1280x720 @ 30fps using `Picamera2`)
-  **Storage to USB Drive** (organized by date, plug-and-play)
-  **Crash Detection** (via SW-420 vibration sensor and GPIO)
-  **Alert Notification** via Email with the attached crash video
-  **Auto Start on Boot** using `systemd` services
-  **Timestamps** for file naming and email body
-  Power-on → Record → Detect → Alert (No human intervention)

---

## 🧰 Tech Stack

### 🔧 Hardware
- Raspberry Pi 3 Model B
- Raspberry Pi Camera Module Rev 1.3 (5MP)
- SW-420 Vibration Sensor Module
- USB Flash Drive (≥16GB)
- MicroSD Card (≥16GB)
- Breadboard, Jumper Wires

### 💻 Software
- Python 3
- Picamera2 (`libcamera`)
- RPi.GPIO or gpiozero
- `smtplib`, `email.mime` for mail alerts
- Raspberry Pi OS Lite (32-bit recommended)
- `systemd`, `crontab`

---
<h2>The Complete and detailed report of this whole project can be found in the (`report/RPI Dashcam.pdf`) <a href="./report/RPI Dashcam.pdf">Here</a>.</h2>


