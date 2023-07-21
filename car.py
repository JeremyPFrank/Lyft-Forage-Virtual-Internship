from abc import ABC, abstractmethod
from serviceable import serviceable

class Car(ABC):
    def __init__(self, engine, battery):
        car_engine = engine
        car_battery = battery

    @abstractmethod
    def needs_service(self):
        if car_engine.needs_service() or car_battery.needs_service():
            return True
        return False
