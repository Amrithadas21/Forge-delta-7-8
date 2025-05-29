import RPi.GPIO as GPIO
import time

# --- GPIO Setup ---
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Stepper motor pins
STEPPER_PINS = {
    'motor1': {'step': 17, 'dir': 27},
    'motor2': {'step': 22, 'dir': 23},
    'motor3': {'step': 24, 'dir': 25}
}

# Setup outputs for motors
for motor in STEPPER_PINS.values():
    GPIO.setup(motor['step'], GPIO.OUT)
    GPIO.setup(motor['dir'], GPIO.OUT)

def move_all_motors(steps=3400, delay=0.0005, direction=GPIO.HIGH):
    # Set direction for all motors
    for motor in STEPPER_PINS.values():
        GPIO.output(motor['dir'], direction)

    # Move all motors together step-by-step
    for _ in range(steps):
        for motor in STEPPER_PINS.values():
            GPIO.output(motor['step'], GPIO.HIGH)
        time.sleep(delay)
        for motor in STEPPER_PINS.values():
            GPIO.output(motor['step'], GPIO.LOW)
        time.sleep(delay)

try:
    # Move motors forward
    move_all_motors(direction=GPIO.HIGH)
    time.sleep(1)
    # Move motors backward
    move_all_motors(direction=GPIO.LOW)
finally:
    GPIO.cleanup()
