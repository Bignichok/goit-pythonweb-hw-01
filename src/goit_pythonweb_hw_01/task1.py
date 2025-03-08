from abc import ABC, abstractmethod
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class Vehicle(ABC):
    def __init__(self, make: str, model: str, spec: str):
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model} {self.spec} двигун запущено.")


class Morotcycle(Vehicle):
    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model} {self.spec} мотор заведено.")


class VehicleFactory:
    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Morotcycle:
        pass


class USAFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "виробництва США")

    def create_motorcycle(self, make: str, model: str) -> Morotcycle:
        return Morotcycle(make, model, "виробництва США")


class EuropeFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "виробництва Європа")

    def create_motorcycle(self, make: str, model: str) -> Morotcycle:
        return Morotcycle(make, model, "виробництва Європа")


if __name__ == "__main__":
    usa_factory = USAFactory()
    europe_factory = EuropeFactory()

    car = usa_factory.create_car("Ford", "Focus")
    motorcycle = europe_factory.create_motorcycle("Yamaha", "FZ6")

    car.start_engine()
    motorcycle.start_engine()
