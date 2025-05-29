import RPi.GPIO as GPIO
import time

# --- GPIO Setup ---
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define your stepper motor pins and limit switch pins
STEPPER_PINS = {
    'motor1': {'step': 17, 'dir': 27},
    'motor2': {'step': 22, 'dir': 23},
    'motor3': {'step': 24, 'dir': 25}
}

# Limit switches: each motor has a 'min' and 'max' switch
LIMIT_SWITCH_PINS = {
    'motor1': {'min': 5,  'max': 6},
    'motor2': {'min': 13, 'max': 19},
    'motor3': {'min': 26, 'max': 21}
}

# Setup outputs for motors
for motor in STEPPER_PINS.values():
    GPIO.setup(motor['step'], GPIO.OUT)
    GPIO.setup(motor['dir'], GPIO.OUT)

# Setup inputs for limit switches (pull-up resistors)
for switches in LIMIT_SWITCH_PINS.values():
    GPIO.setup(switches['min'], GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(switches['max'], GPIO.IN, pull_up_down=GPIO.PUD_UP)

# --- Motor Control with Limit Checking ---
def test_motor_with_limits(motor_name, steps=3400, delay=0.0005):
    pins = STEPPER_PINS[motor_name]
    limits = LIMIT_SWITCH_PINS[motor_name]
    print(f"Testing {motor_name} with limit switches")

    # Rotate forward until max switch is hit or steps exhausted
    GPIO.output(pins['dir'], GPIO.HIGH)
    for step_count in range(steps):
        if GPIO.input(limits['max']) == GPIO.LOW:  # Limit switch pressed (active low)
            print(f"{motor_name} max limit hit at step {step_count}")
            break
        GPIO.output(pins['step'], GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(pins['step'], GPIO.LOW)
        time.sleep(delay)
    time.sleep(0.5)

    # Rotate backward until min switch is hit or steps exhausted
    GPIO.output(pins['dir'], GPIO.LOW)
    for step_count in range(steps):
        if GPIO.input(limits['min']) == GPIO.LOW:
            print(f"{motor_name} min limit hit at step {step_count}")
            break
        GPIO.output(pins['step'], GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(pins['step'], GPIO.LOW)
        time.sleep(delay)
    time.sleep(0.5)

# --- Main Execution ---
if __name__ == "__main__":
    try:
        # Test each motor individually
        for name in STEPPER_PINS.keys():
            test_motor_with_limits(name)
    finally:
        GPIO.cleanup()


