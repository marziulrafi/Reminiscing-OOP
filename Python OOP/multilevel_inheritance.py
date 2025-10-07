class Grandfather:
    def land(self):
        print("Has 10 acres of land")

class Father(Grandfather):
    def house(self):
        print("Has a big house")

class Son(Father):
    def bike(self):
        print("Has a new bike")

s = Son()
s.land()   # from Grandfather
s.house()  # from Father
s.bike()   # from Son
