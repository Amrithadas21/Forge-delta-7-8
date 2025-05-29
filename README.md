DELTA TEAM

DELTA -SOFTWARE:
Raspberry Pi Stepper Motor & Camera Calibration Utilities

This repository contains Python scripts and resources for stepper motor control using GPIO on Raspberry Pi, as well as a camera calibration and video preprocessing pipeline using OpenCV and the PiCamera2 module.


 📁 Repository Contents

| File                    | Description                                                                                                      |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `latest_calib.py`       | Performs camera calibration using chessboard images. Saves undistorted outputs and calibration matrices.         |
| `same sync movement.py` | Drives 3 stepper motors simultaneously in a synchronized manner.                                                 |
| `diff movement.py`      | Controls stepper motors independently with limit switch safety checks.                                           |
| `streams.py`            | Captures live video from PiCamera2, applies preprocessing (CLAHE, denoise, sharpen), and saves processed frames. |
| `Motor controls.docx`   | Documentation explaining the difference between same and independent motor movements.                            |
| `corners.jpg`           | Sample chessboard image used for camera calibration.                                                             |

---

🛠️ Requirements

* Raspberry Pi with GPIO and PiCamera support
* Python 3.x
* Libraries:

  * `RPi.GPIO`
  * `picamera2`
  * `opencv-python`
  * `numpy`





DELTA – HARDWARE: Delta Robot Arm with Conveyor Mechanism
This setup includes the Delta Robot mechanical frame, stepper motors, and a conveyor belt system. It is designed for high-speed, precise object manipulation and sorting tasks. The structure is lightweight, modular, and integrated with sensors for smart automation.

📦 Hardware Components
Component	Description
Delta Robot Frame	Lightweight 3-arm parallel-link mechanism designed for high-speed pick-and-place.
Stepper Motors (x3)	NEMA 17 stepper motors controlling the delta arms, allowing synchronized movements.
Servo Motor (End Effector)	For precise gripping and object manipulation.
Limit Switches	Safety switches to detect end positions and avoid overtravel.
Conveyor Belt System	DC motor–driven conveyor belt to bring items into the robot's workspace.
Motor Driver Boards	A4988 or DRV8825 drivers for controlling stepper motors.
Raspberry Pi (Interface)	Acts as the main controller connecting hardware with software utilities.
Power Supply	12V regulated supply for motors and control electronics.
Frame & Mounts	Acrylic/Aluminum frame to support robot and conveyor belt assembly.

🛠️ Assembly & Configuration Notes
Parallel Kinematics used for faster and more precise movement.

Conveyor belt is positioned beneath the robot’s workspace for continuous object feeding.

End effector is interchangeable based on object type (suction cup, gripper, magnet).

All wiring is connected to a central Raspberry Pi, which interfaces with motor drivers and sensors.

Limit switches ensure safe zeroing and homing of motors before task execution.

⚙️ Control & Integration
Controlled via Python scripts from the Raspberry Pi.

Synchronization between conveyor movement and delta arm is done using GPIO triggers and camera input.

Integration with camera calibration pipeline allows object detection and positioning.# Delta-Robot-Hardware








