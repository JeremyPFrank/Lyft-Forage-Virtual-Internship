from tire.octoprime_tire import OctoprimeTire
import unittest

class TestOctoprimeTire(unittest.TestCase):
  def does_need_service(self):
    tire=OctoprimeTire([0.9,0.8,0.89,0.91])
    self.assertTrue(engine.needs_service())
  def not_need_service(self):
    tire=OctoprimeTire([0.1,0.5,0.4,0.5])
    self.assertTrue(engine.needs_service())
