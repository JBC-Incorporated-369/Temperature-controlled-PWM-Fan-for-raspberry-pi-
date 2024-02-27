import RPi.GPIO as GPIO
import time
import os

# Setup GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

# Set the GPIO pin for the fan
fan_pin = 18
GPIO.setup(fan_pin, GPIO.OUT)

# Create PWM instance
fan_pwm = GPIO.PWM(fan_pin, 100)  # PWM frequency set to 100 Hz

# Define temperature threshold and fan power
on_threshold = 40  # Fan turns on above this temperature
low_power_duty_cycle = 20  # Fan runs at 20% power when below on_threshold

try:
    fan_pwm.start(0)  # Start PWM with duty cycle 0
    while True:
        # Read CPU temperature
        temp = float(os.popen("vcgencmd measure_temp").readline().replace("temp=","").replace("'C\n",""))

        # Adjust fan speed based on temperature
        if temp > on_threshold:
            fan_pwm.ChangeDutyCycle(100)  # Fan at full speed
        else:
            fan_pwm.ChangeDutyCycle(low_power_duty_cycle)  # Fan at 20% power

        time.sleep(5)  # Check temperature every 5 seconds

except KeyboardInterrupt:
    fan_pwm.stop()  # Stop PWM
    GPIO.cleanup()  # Clean up GPIO on Ctrl+C exit
