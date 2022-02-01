import RPi.GPIO as GPIO
from flask import Flask, render_template, request
import traceback
import logging
from database.service import add
from sensors import lcd, servo, weight

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def home():
  lcd.enable()
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
      is_running = True
      lcd.message("Start\nfeeding...", 3)
      while is_running:
        val = float(round(weight.get_weight()))
        lcd.message(str(val), 1)

        servo.run(2)
        servo.stop(0.5)

        while grams - 5 <= val:
          servo.stop(0.0)
          is_running = False
          break
      lcd.finish_message()
    except KeyboardInterrupt:
      servo.stop(0.0)
      GPIO.cleanup()
    return render_template("main.html")

  except Exception:
    servo.stop(0.0)
    GPIO.cleanup()
    logging.error(traceback.format_exc())

if __name__ == "__main__":
  app.run(host='172.16.14.144')
