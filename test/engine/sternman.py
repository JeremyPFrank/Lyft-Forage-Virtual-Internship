from engine.sternman_engine import SternmanEngine
import unittest

class TestSternmanEngine(unittest.TestCase):
  def does_need_service(self):
    engine=SternmanEngine(True)
    self.assertTrue(engine.needs_service())
  def not_need_service(self):
    engine=SternmanEngine(False)
    self.assertTrue(engine.needs_service())
