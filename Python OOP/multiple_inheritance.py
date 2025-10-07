class Father:
    def gardening(self):
        print("I love gardening")

class Mother:
    def cooking(self):
        print("I love cooking")

class Child(Father, Mother):
    def play(self):
        print("I love playing")

c = Child()
c.gardening()  # from Father
c.cooking()    # from Mother
c.play()       # from Child
