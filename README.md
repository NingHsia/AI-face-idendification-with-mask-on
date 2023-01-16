# AI final project: Face Identification with Mask On
Because of the pandemic, the government implemented strict control over access to nearly all locations. To promoted the efficiency and user-friendliness of the check-in process, we tackled the use of AI with masked face identification and successfully trained the algorithm with a mask detection model, a masked face recognition model, and a gesture recognition model to create an access control system that could detect and record body temperatures and deny access to visitors who are not in the preset database.


## Requirement
opencv-python 4.5.1

tensorflow 2.5

keras 2.5

Arduino

## Usage
connect MLX90614 module to Arduino

connect Arduino to computer

compile and run MLX90614_Module.ino

add images to `/imgs` with filename as your name

`python3 ver1.py`

`python3 ver2.py`
