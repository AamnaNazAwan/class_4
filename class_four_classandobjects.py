#CLASS: A blueprint for creating objects
#OBJECT: An instance of class
#ATTRIBUTES: Data stored in an object
#METHODS: Functions that belong to an object


'''(1)class definition
(2)initiLIZER METHOD
(3)DESCRIBE METHOD
(4)CREATING OBJECT
(5)ACCESSING METHOD'''


'''class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def describe(self):
     return f"{self.name} is {self.age} years old"

dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)

print(dog1.describe())
print(dog2.describe())



class car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        return f"This car is a {self.year} {self.make} {self.model}"

    # for updating anything

    def update_year(self, new_year):
        self.year = new_year

    def update_model(self, new_model):
        self.year = new_model



car1 = car('honda','civic',2013)
car2 = car('toyota','corola',2018)

print(car1.description())
print(car2.description())


car1.update_year(2020)
car1.update_model('city')
print(car1.description())'''


class car:
    number_of_wheels = 4
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        return f"This car is a {self.year}{self.make}{self.model}"

    @classmethod
    def update_number_of_wheels(cls,new_number):
        cls.number_of_wheels = new_number

    @staticmethod
    def is_motor_vehicle():
        return True

car1 = car('honda','civic',2013)
car2 = car('toyota','corola',2018)

print(car1.description())
print(car2.description())


#accessing class variables
print(car.number_of_wheels)

#changing class variable using class method
car.update_number_of_wheels(6)
print(car.number_of_wheels)

#accessing static method
print(car.is_motor_vehicle())

#foe destructor we use [def __del__()]


class employee:
    total_employees = 0

    def __init__(self,name):
        self.name = name
        employee.total_employees +=1


    @classmethod
    def get_total_employees(cls):
        return cls.total_employees


emp1 = employee('ALICE')
emp2 = employee('BOB')
emp3 = employee('CHARLIE')


print(employee.get_total_employees())


