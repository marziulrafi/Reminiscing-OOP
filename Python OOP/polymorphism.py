class Student:
    def __init__(self, name, current_class, id):
        self.name = name
        self.id = id
        self.current_class = current_class

    # This method provides the string representation of a Student object
    def __repr__(self) -> str:
        return f'Student with name: {self.name}, class: {self.current_class}, id:{self.id}'


class Teacher:
    def __init__(self, name, subject, id) -> None:
        self.name = name
        self.subject = subject
        self.id = id

    # This method provides the string representation of a Teacher object
    def __repr__(self) -> str:
        return f'Teacher: {self.name}, subject: {self.subject}'


class School:
    def __init__(self, name) -> None:
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self, name, subject):
        # Generate ID for the new teacher
        id = len(self.teachers) + 101
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)
    
    def enroll(self, name, fee):
        if fee < 6500:
            return f'{name} could not be enrolled: not enough fee (required: 6500)'
        else:
            # Generate ID for the new student
            id = len(self.students) + 1
            student = Student(name, 'C', id)
            self.students.append(student)
            return f'{name} is enrolled with id: {id}, extra money {fee - 6500}'

   
    def __repr__(self) -> str:
        # Start building the multi-line string
        result = f'Welcome to {self.name}\n'
        
        # Add Teachers section
        result += '--------OUR TEACHERS--------\n'
        for teacher in self.teachers:
            # Calls the Teacher's __repr__ method
            result += str(teacher) + '\n' 
            
        # Add Students section
        result += '--------OUR STUDENTS--------\n'
        for student in self.students:
            # Calls the Student's __repr__ method
            result += str(student) + '\n'
            
        return result




# --- Execution ---

phitron = School('Phitron')

# Enroll students (some fail, some succeed)
print(phitron.enroll('alia', 5200)) # Fails
print(phitron.enroll('rani', 8000))
print(phitron.enroll('aishwaraiya', 7000))
print(phitron.enroll('vaijaan', 90000))

print("-" * 30)

# Add teachers
phitron.add_teacher('Tom Cruise', 'Algo')
phitron.add_teacher('Decap', 'DS')
phitron.add_teacher('AJ', 'Database')

# Prints the string returned by School's __repr__
print("-" * 30)
print(phitron)