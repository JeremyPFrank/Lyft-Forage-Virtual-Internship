from Battery.SpindlerBattery import SpindlerBattery
import unittest

class TestSpindlerBattery(unittest.TestCase):
  def does_need_service(self):
    current_date = date.fromisoformat("2023-07-21")
    last_service_date = date.fromisoformat("2005-02-04")
    battery=SpindlerBattery(current_date,last_service_date)
    self.assertTrue(battery.needs_service())
  def not_need_service(self):
    current_date = date.fromisoformat("2023-07-21")
    last_service_date = date.fromisoformat("2023-05-20")
    battery=v(current_date,last_service_date)
    self.assertTrue(battery.needs_service())

