import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac=[8,11,7,1,0,5,12,6]
num=[1,1,1,1,1,1,1,1]
numb=0
GPIO.setup(dac,GPIO.OUT)
GPIO.output(dac,num)
time.sleep(20)
GPIO.output(dac,0)
GPIO.cleanup()
