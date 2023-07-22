from tire.carrigan_tire import CarriganTire
import unittest

class TestCarriganTire(unittest.TestCase):
  def does_need_service(self):
    tire=CarriganTire([0.1,0.5,0.89,0.91])
    self.assertTrue(engine.needs_service())
  def not_need_service(self):
    tire=CarriganTire([0.1,0.5,0.89,0.88])
    self.assertTrue(engine.needs_service())
