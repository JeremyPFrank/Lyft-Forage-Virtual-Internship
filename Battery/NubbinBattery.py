from Battery.battery import Battery

class NubbinBattery(Battery):
  def _init_(self, last_service_date, current_date):
    self.last_service_date = last_service_date
    self.current_date = current_date
  def needs_service(self):
    service_date = last_service_date.replace(year=last_service_date.year + 4)
    if current_date >= service_date
      return True
    return False

