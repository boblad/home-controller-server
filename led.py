import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)

servo = GPIO.PWM(27, 50)
servo.start(7.5)

light_is_on = False

def turn_light_on():
    servo.ChangeDutyCycle(9.5)
    time.sleep(0.6)

def turn_light_off():
    servo.ChangeDutyCycle(5.5)
    time.sleep(0.6)

try:
    while True:
	input_state = GPIO.input(15)
	print input_state
        if input_state == False and light_is_on == False:
            print "here 1"
	    light_is_on = True
            turn_light_on()
        elif input_state == False and light_is_on == True:
            print "here 2"
	    light_is_on = False
            turn_light_off()
	time.sleep(0.05)

except KeyboardInterrupt:
    servo.stop()
    GPIO.cleanup()
