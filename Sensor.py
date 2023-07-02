import RPi.GPIO as GPIO
import time

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
TRIG = 11
ECHO = 12
BUZZER = 27
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(BUZZER, GPIO.OUT)

# Measure distance
def measure_distance():
    # Send ultrasonic pulse
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    # Measure echo time
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
    # Calculate distance in cm
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    return distance

# Main loop
while True:
    distance = measure_distance()
    print(distance)
    if distance >= 0.1 and distance <= 150:
        # Object detected within 1-150cm range
        # Calculate buzzer frequency based on distance
        buzzer_frequency = int(1 / (distance / 100))
        # Play buzzer sound
        GPIO.output(BUZZER, True)
        time.sleep(buzzer_frequency)
        GPIO.output(BUZZER, False)
    time.sleep(0.1)
