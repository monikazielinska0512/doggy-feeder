import time
from hx711.hx import HX711


class WeightScale:
    def __init__(self):
        self.d_out_pin = 5
        self.sck_pin = 6
        self.run_calibration = False
        self.reference_unit = -792054.8888888889/400
        self.hx = HX711(5, 6)
        self.hx.set_reading_format("MSB", "MSB")
        self.hx.set_reference_unit(self.reference_unit)
        self.hx.reset()
        self.hx.tare()

    def get_weight(self):
        val = self.hx.get_weight(5)
        self.hx.power_down()
        self.hx.power_up()
        time.sleep(0.001)
        return val

    def tare(self):
        self.hx.tare()
