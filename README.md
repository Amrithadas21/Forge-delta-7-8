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









