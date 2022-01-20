import time
from adafruit_lcd.Adafruit_CharLCD import Adafruit_CharLCD
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

class LCD:
    def __init__(self):
        self.rs = 25
        self.en = 24
        self.d4 = 23
        self.d5 = 17
        self.d6 = 26
        self.d7 = 22
        self.backlight = 4
        self.columns = 16
        self.rows = 2
        self.lcd = Adafruit_CharLCD(self.rs, self.en,
                                    self.d4, self.d5,
                                    self.d6, self.d7,
                                    self.columns, self.rows,
                                    self.backlight)

    def message(self, message, t):
        self.lcd.message(message)
        time.sleep(t)
        self.lcd.clear()

    def finish_message(self):
        self.message("Finish\nfeeding", 2)
        self.message("Enjoy!", 2)
        self.lcd.enable_display(False)
