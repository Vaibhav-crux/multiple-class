class Car():
    def __init__(self,name,model,year):
        self.name=name
        self.model=model
        self.year=year
        self.odometer_reading=0
    def information(self):
        car_info="Name:",self.name,"Model:",self.model,"Year:",self.year
        return car_info
    def odometer(self):
        print("This car has",self.odometer_reading,"miles")
    def update_odometer(self,milage):
        if(milage>=self.odometer_reading):
            self.odometer_reading=milage
        else:
            print("Can't roll back odometer")
            
class Electriccar(Car):
    def __init__(self,name,model,year):
        super().__init__(name,model,year)
        super().odometer()
        
class Bike(Car):
    def __init__(self,name,model,year):
        super().__init__(name,model,year)
               
newcar=Car("Audi","AUX125","2020")
#newcar.odometer_reading=int(input("Millage:"))  UPDATE ODOMETER
#newcar.update_odometer(int(input("Update millage:")))   #UPDATE ODOMETER
print(newcar.information())
newcar.odometer()

elect_c=Electriccar("Tesla","A4","2022")
print(elect_c.information())

bi=Bike("Ola","TY4","2021")
print(bi.information())
