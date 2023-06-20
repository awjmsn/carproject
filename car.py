"""A class used to represent a car"""


class Car:
  """A simple attempt to represent a car."""

  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0

  def get_descriptive_name(self):
    long_name = f"{self.year} {self.make} {self.model}"
    return long_name.title()

  def read_odometer(self):
    print(f"This car has {self.odometer_reading} miles on it.")

  def update_odometer(self, mileage):
    if mileage >= self.odometer_reading:
      self.odometer_reading = mileage
    else:
      print("You can't roll back an odometer!")

  def increment_odometer(self, miles):
    self.odometer_reading += miles


class Battery:
  """models an electric car battery"""

  def __init__(self, battery_size=75):
    """Initialize the battery's attributes"""
    self.battery_size = battery_size

  def describe_battery(self):
    """Describes the battery"""
    print(f"This car has a {self.battery_size}-KWh battery.")

  def upgrade_battery(self):
    if self.battery_size < 100:
      self.battery_size = 100
      print('Battery is now upgraded')
    else:
      print("your battery is already upgraded")


class ElectricCar(Car):
  """Represents all aspects of a car, specific to electric vehicles"""

  def __init__(self, make, model, year):
    """Initialize attributes of the parent class."""
    super().__init__(make, model, year)
    self.battery = Battery()


