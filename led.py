import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

servo = GPIO.PWM(18, 50)
servo.start(7.5)

light_is_on = False

def turn_light_on():
    light_is_on = True
    servo.ChangeDutyCycle(9.5)
    time.sleep(1)

def turn_light_off():
    light_is_on = False
    servo.ChangeDutyCycle(5.5)
    time.sleep(1)

try:
    while True:
        # turn_light_on()
        # turn_light_off()
        if GPIO.input(15) == 1:
            print "down"
        if GPIO.input(15) == 1:
            print "here 1"
            turn_light_on()
        elif GPIO.input(15) == 1:
            print "here 2"
            turn_light_off()

except KeyboardInterrupt:
    servo.stop()
    GPIO.cleanup()
