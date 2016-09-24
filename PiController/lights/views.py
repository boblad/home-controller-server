from django.http import HttpResponse
import RPi.GPIO as GPIO
import time
import threading

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)

servo = GPIO.PWM(27, 50)
servo.start(7.5)

run_auto = True
light_is_on = False

def start_auto():
    global light_is_on
    while(run_auto == True):
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

auto_thread = threading.Thread(target=start_auto, args = ())
auto_thread.daemon = True
auto_thread.start()

def turn_light_on():
    servo.ChangeDutyCycle(9.5)
    time.sleep(0.6)

def turn_light_off():
    light_is_on = False
    servo.ChangeDutyCycle(5.5)
    time.sleep(0.6)

def on(request):
    global run_auto
    global light_is_on
    global auto_thread
    run_auto = False
    print 'hello'
    time.sleep(0.09)
    if light_is_on == True:
        light_is_on = False
        turn_light_off()
    else:
        light_is_on = True
        turn_light_on()
    run_auto = True
    auto_thread = threading.Thread(target=start_auto, args = ())
    auto_thread.daemon = True
    auto_thread.start()
    return HttpResponse("on")

def off(request):
    global run_auto
    global light_is_on
    global auto_thread
    run_auto = False
    time.sleep(0.09)
    light_is_on = False
    turn_light_off()
    run_auto = True
    auto_thread = threading.Thread(target=start_auto, args = ())
    auto_thread.daemon = True
    auto_thread.start()
    return HttpResponse("off")

