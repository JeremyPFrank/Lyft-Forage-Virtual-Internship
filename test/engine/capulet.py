from engine.capulet_engine import CapuletEngine
import unittest

class TestCapuletEngine(unittest.TestCase):
  def does_need_service(self):
    engine=CapuletEngine(30001,0)
    self.assertTrue(engine.needs_service())
  def not_need_service(self):
    engine=CapuletEngine(29000,0)
    self.assertTrue(engine.needs_service())
