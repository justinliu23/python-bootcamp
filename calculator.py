import random

class Calculator():
  def __init__(self):
    self.num1 = random.randint(1, 10)
    self.num2 = random.randint(1, 10)

  def add(self, num1, num2):
    return num1 + num2
  def subtract(self, num1, num2):
    return num1 - num2
  def multiply(self, num1, num2):
    return num1 * num2
  def divide(self, num1, num2):
    return num1 / num2

  def get_num1(self):
    return self.num1
  def get_num2(self):
    return self.num2
  
  def set_num1(self, new_num1):
    self.num1 = new_num1
  def set_num2(self, new_num2):
    self.num2 = new_num2

calc = Calculator()
num1 = calc.get_num1()
num2 = calc.get_num2()
print('num1', num1)
print('num2', num2)
print(calc.multiply(num1, num2))