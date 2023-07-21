from Battery.battery import Battery
from Battery.NubbinBattery import NubbinBattery
from Battery.SpindlerBattery import SpindlerBattery
from engine.engine import Engine
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from car import Car

class CarFactory:

  def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int): 
    engine = CapuletEngine(current_mileage,last_service_mileage)
    battery = SpindlerBattery(current_date,last_service_date)
    return Car(engine,battery)
  def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int): 
    engine = WilloughbyEngine(current_mileage,last_service_mileage)
    battery = SpindlerBattery(current_date,last_service_date)
    return Car(engine,battery)
  def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool): 
    engine = SternmanEngine(warning_light_on)
    battery = SpindlerBattery(current_date,last_service_date)
    return Car(engine,battery)
  def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
    engine = WilloughbyEngine(current_mileage,last_service_mileage)
    battery = NubbinBattery(current_date,last_service_date)
    return Car(engine,battery)
  def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
    engine = CapuletEngine(current_mileage,last_service_mileage)
    battery = NubbinBattery(current_date,last_service_date)
    return Car(engine,battery)
