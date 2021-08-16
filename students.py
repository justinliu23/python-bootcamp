class Student():
  def __init__(self, first_name, last_name, id, grade):
    self.first_name = first_name
    self.last_name = last_name
    self.id = id
    self.grade = grade
  
  def print_description(self):
    print(self.first_name + " " + self.last_name + " is in " + str(self.grade) + "th grade. Their ID # is " + str(self.id))

  def get_id(self):
    return self.id


stud1 = Student('John', 'Smith', 124147, 10)
stud2 = Student('Mike', 'Wheeler', 873425, 11)
stud3 = Student('Michelle', 'Lee', 634533, 9)

students = {}
students[stud1.get_id()] = stud1
students[stud2.get_id()] = stud2
students[stud3.get_id()] = stud3

for student in students.values():
  print(student.print_description())