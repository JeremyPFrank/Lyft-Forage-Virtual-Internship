from serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, engine, battery):
        self.car_engine = engine
        self.car_battery = battery

    def needs_service(self):
        if car_engine.needs_service() or car_battery.needs_service():
            return True
        return False
