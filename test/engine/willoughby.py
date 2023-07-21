from engine.willoughby_engine import WilloughbyEngine
import unittest

class TestWilloughbyEngine(unittest.TestCase):
  def does_need_service(self):
    engine=WilloughbyEngine(60001,0)
    self.assertTrue(engine.needs_service())
  def not_need_service(self):
    engine=WilloughbyEngine(59000,0)
    self.assertTrue(engine.needs_service())
