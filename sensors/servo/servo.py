import RPi.GPIO as GPIO
import pigpio
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pin: int = 18
pi: pigpio.pi = pigpio.pi()
GPIO.setup(pin, GPIO.OUT)

def run(time: float):
  pi.set_servo_pulsewidth(pin, 1499)
  sleep(time)

def stop(time: float):
  pi.set_servo_pulsewidth(pin, 1511)
  sleep(time)
