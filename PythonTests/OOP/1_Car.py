# OOP

class Vehicle(object):
    """
    __init__ Takes two data attributes the name
    of the car, The Year in which the car was
    made, Aswell as the horsepower and torque.
    """
    # The data attributes.
    def __init__(self, vehicleName, vehicleModel, vehicleHorsepower, vehicleTorque):
        self.vehicleName = vehicleName
        self.vehicleModel = vehicleModel
        self.vehicleHorsepower = vehicleHorsepower
        self.vehicleTorque = vehicleTorque

    # Prints Info about the car.
    def __str__(self):
        return "Name: " + self.vehicleName + "\n" + "Model: " + self.vehicleModel

    def horsepower(self):
        return self.vehicleTorque * self.vehicleHorsepower / 5252

# Initialize a variable with the newly created object "Vehicle"
Mustang = Vehicle("Mustange", "1996", 150, 4500)

# By using __str__ we are able to print correctly.
print(Mustang)

# Able to create methods and use them.
print(Mustang.horsepower())
