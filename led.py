import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

servo = GPIO.PWM(18, 50)
servo.start(7.5)

try:
    while True:
        servo.ChangeDutyCycle(7.5)
        time.sleep(1)
        servo.ChangeDutyCycle(12.5)
        time.sleep(1)
        servo.ChangeDutyCycle(2.5)
        time.sleep(1)

except KeyboardInterrupt:
    servo.stop()
    GPIO.cleanup()
