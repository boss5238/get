import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(24,GPIO.IN)
if (GPIO.input(24)==1):
    GPIO.output(21,1)
else:
    GPIO.output(21,0)


