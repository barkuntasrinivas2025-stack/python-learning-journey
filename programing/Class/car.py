class Car:
    def __init__(self,year,model,brand):
        self.year=year
        self.model=model
        self.brand=brand
    def drive(self):
        # self.brand=brand
        print(f"this working is good {self.brand}")
    def engine(self):
        print("engine is in working condition")