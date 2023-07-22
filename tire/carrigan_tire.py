from tire.tire import Tire

class CarriganTire(Tire):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
      for tire in tire_wear:
        if tire>=0.9:
          return True
      return False
