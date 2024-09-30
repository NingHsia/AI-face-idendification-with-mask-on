# AI-based access control system optimized for masked facial recognition
With the advent of the COVID-19 pandemic, governments worldwide implemented strict access control measures to ensure public safety. To improve efficiency and user experience during the check-in process, this project leverages the Google FaceNet model for masked facial recognition, integrating body temperature monitoring to address the challenges of mask-wearing and health screening. 

## Features
- Masked Face Recognition: Accurately identifies users even while wearing masks.
- Temperature Monitoring: Measures body temperature to detect potential fever.
- Access Control: Denies entry for users not present in the authorized database or with elevated body temperatures.

## System Requirements
- Python Libraries:
  - opencv-python==4.5.1
  - tensorflow==2.5
  - keras==2.5
- Hardware:
  - MLX90614 (Infrared temperature sensor)
  - Arduino (for interfacing with the MLX90614 sensor)

## Setup Instructions
### 1. Hardware Setup
1. Connect the MLX90614 temperature sensor to the Arduino.
2. Connect the Arduino to your computer using a USB cable.
### 2. Software Setup
1. Install the required Python packages by running:
   ```
   pip install opencv-python==4.5.1 tensorflow==2.5.0 keras==2.5.0
   ```
3. Upload the Arduino script:
    - Open the MLX90614_Module.ino file in the Arduino IDE.
    - Compile and upload the code to your Arduino board.
### 3. Image Database Setup
1. Add images of users to the /imgs directory.
2. Ensure each image file is named with the user's name (e.g., JohnDoe.jpg).
### 4. Running the System
You can run different versions of the system as follows:
- To run the honesty-based system:
  ```
  python3 ver1.py
  ```
- To run the strict restriction system:
  ```
  python3 ver2.py
  ```
