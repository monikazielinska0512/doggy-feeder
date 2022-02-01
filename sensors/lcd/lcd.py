from time import sleep
from adafruit_lcd.Adafruit_CharLCD import Adafruit_CharLCD
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

lcd = Adafruit_CharLCD(rs=25, en=24, d4=23, d5=17, d6=26, d7=22, cols=16, lines=2, backlight=4)

def enable():
  lcd.enable_display(True)

def message(message: str, time: float):
  sleep(time)
  lcd.message(message)
  lcd.clear()

def finish_message():
  message("Finish\nfeeding", 2)
  message("Enjoy!", 2)
  lcd.enable_display(False)
