import time
import RPi.GPIO as GPIO
import pigpio
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


class Servo:
    def __init__(self):
        self.pin = 18
        GPIO.setup(self.pin, GPIO.OUT)
        self.pi = pigpio.pi()

    def run(self, t):
        self.pi.set_servo_pulsewidth(self.pin, 1499)
        time.sleep(t)

    def stop(self, t):
        self.pi.set_servo_pulsewidth(self.pin, 1511)
        time.sleep(t)
