class Student:
    def __init__(self, name, marks):
        # The underscore means "private" (by convention)
        self._name = name
        self._marks = marks

    #Getter
    @property
    def marks(self):
        """Getter method - called when you access student.marks"""
        return self._marks

    #Setter
    @marks.setter
    def marks(self, value):
        """Setter method - called when you assign to student.marks"""
        if value < 0 or value > 100:
            print("nvalid marks! Must be between 0 and 100.")
        else:
            self._marks = value
            print("Marks updated successfully!")

    # Another getter (for demonstration)
    @property
    def name(self):
        return self._name





s = Student("Rafi", 85)
print(s.name)          # calls @property -> prints "Rafi"
print(s.marks)         # calls getter -> prints 85

s.marks = 95           # calls setter -> updates marks
print(s.marks)         # 95

s.marks = -10          # invalid input -> shows error message
