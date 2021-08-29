import uuid
import pandas as pd
import json




print('Vehicle Inventory')
class Vehicle_Screen:
    def __init__(self):
        self._id = ''
        self._brand = ''
        self._horsepower = 0
        self._model = ''
        self._price = 0
    def add_car(self):
        try:
            self._id = uuid.uuid4().hex[:8]
            self._brand = input('Enter vehicle brand: ')
            self._horsepower = int(input('Enter vehicle horsepower: '))
            self._model = input('Enter vehicle model: ')
            self._price = int(input('Enter vehicle price: '))
            return True
        except ValueError:
            print('Please try entering vehicle information again using only whole numbers for mileage and year')
            return False
    def __str__(self):
        return '\t'.join(str(a) for a in [self._id, self._brand, self._horsepower, self._model, self._price])

class Car_Inventory:
    def __init__(self):
        self.cars = []
    def add_car(self):
        vehicle = Vehicle_Screen()
        if vehicle.add_car() == True:
            self.cars.append(vehicle)
            print ()
            print('This vehicle has been added, Thank you')
    def Display_Car_Inventory(self):
        print('\t'.join(['', 'ID', 'Brand', 'Horsepower', 'Model', 'Price']))
        for idx, vehicle in enumerate(self.cars):
            print(idx + 1, end='\t')
            print(vehicle)

inventory = Car_Inventory()
while True:

    print('Choice 1: Add Vehicle to Inventory')
    print('Choice 2: Delete Vehicle from Inventory')
    print('Choice 3: View Current Inventory')
    print('Choice 4: Update Vehicle in Inventory')
    print('Choice 5: Export Current Inventory')
    print('Choice 6: Convert Csv')
    print('Choice 7: Quit')
    User_Choice=input('Please Enter your Choice from one of the above options: ')
    if User_Choice== "1":
        #add a vehicle
        inventory.add_car()
    elif User_Choice== '2':
        #delete a vehicle
        if len(inventory.cars) < 1:
            print('Sorry there are no vehicles currently in inventory')
            continue
        inventory.Display_Car_Inventory()
        Products = int(input('Please enter the number associated with the vehicle to be removed: '))
        if Products - 1  > len(inventory.cars):
            print('This is an invalid number')
        else:
            inventory.cars.remove(inventory.cars[Products - 1])
            print ()
            print('This vehicle has been removed')
    elif User_Choice == '3':
        #list all the vehicles
        if len(inventory.cars) < 1:
            print('Sorry there are no vehicles currently in inventory')
            continue
        inventory.Display_Car_Inventory()
    elif User_Choice == '4':
        #edit vehicle
        if len(inventory.cars) < 1:
            print('Sorry there are no vehicles currently in inventory')
            continue
        inventory.Display_Car_Inventory()
        Products = int(input('Please enter the number associated with the vehicle to be updated: '))
        if Products - 1  > len(inventory.cars):
            print('This is an invalid number')
        else:
            auto_vehicle = Vehicle_Screen()
            if auto_vehicle.add_car() == True :
                inventory.cars.remove(inventory.cars[Products - 1])
                inventory.cars.insert(Products - 1, auto_vehicle)
                print ()
                print('This vehicle has been updated')
    elif User_Choice == '5':
        # export inventory to file
        if len(inventory.cars) < 1:
            print('Sorry there are no vehicles currently in inventory')
            continue
        file = open('vehicle_inventory.txt', 'w')
        file.write('\t'.join(['IdCars', 'Brand', 'Horsepower', 'Model', 'Price']))
        file.write('\n')
        for car_v in inventory.cars:
            file.write('%s\n' % car_v)
        file.close()
        print('The vehicle inventory has been exported to a file')
    elif User_Choice == '6':
            #csv coverter
        read_file = pd.read_csv(r'vehicle_inventory.txt')
        read_file.to_csv(r'vehicle_inventory.csv', )
        print('Csv converted')
    elif User_Choice == '7':
        #exit the loop
        print('Goodbye')
        break
    else:
        #invalid user input
        print('This is an invalid input. Please try again.')




