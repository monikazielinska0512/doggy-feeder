import RPi.GPIO as GPIO
from flask import Flask, render_template, request
import traceback
import logging
from database.service import add
from sensors.servo.servo import Servo
from sensors.weight.weight import WeightScale
from sensors.lcd.lcd import LCD

app = Flask(__name__)
app.config['DEBUG'] = True
servo = Servo()
weight = WeightScale()
lcd = LCD()


@app.route("/")
def home():
    lcd.lcd.enable_display(True)
    lcd.message("Welcome..!", 5.0)
    return render_template("main.html")


@app.route("/test", methods=["POST"])
def test():
    weight.tare()
    try:
        name = request.form["name"]
        grams = float(request.form["grams"])
        add(name, grams)
        try:
            stop = 0
            lcd.message("Start\nfeeding...", 3)
            while True:
                if stop == 1:
                    stop = 0
                    break

                val = float(round(weight.get_weight()))
                lcd.message(str(val), 1)

                servo.run(2)
                servo.stop(0.5)

                while grams-5 <= val:
                    servo.stop(0.0)
                    stop += 1
                    if stop == 1: break
            lcd.finish_message()
        except KeyboardInterrupt:
            servo.stop(0.0)
            GPIO.cleanup()
        return render_template("main.html")

    except Exception as e:
        servo.stop(0.0)
        GPIO.cleanup()
        logging.error(traceback.format_exc())


if __name__ == "__main__":
    app.run(host='172.16.14.144')
