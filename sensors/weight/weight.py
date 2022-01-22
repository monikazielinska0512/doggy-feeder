import time
from sensors.weight.hx711 import HX711

weight: HX711 = HX711(dout=5, pd_sck=6)
weight.set_reading_format("MSB", "MSB")
weight.set_reference_unit(reference_unit=-792054.8888888889 / 400)
weight.reset()
weight.tare()

def tare():
  weight.tare()

def get_weight():
  value = weight.get_weight(times=5)
  weight.power_down()
  weight.power_up()
  time.sleep(0.001)
  return value
