from abc import ABC, abstract class

class Serviceable(ABC):
  @abstractmethod
  def needs_service(self):
    pass
