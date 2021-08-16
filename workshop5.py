class Athlete():
  # constructor
  def __init__(self, height, weight, sport):
    self.height = height
    self.weight = weight
    self.sport = sport

  # "void" function
  def print_description(self):
    print("This " + self.sport + " player is " + str(self.height) + " inches tall and " + str(self.weight) + " pounds heavy.")
  
  # setter
  def change_height(self, new_height):
    self.height = new_height

  # getter
  def get_sport(self):
    return self.sport

# create an instance (object) of the Athlete class
athlete1 = Athlete(69, 180, 'football')
athlete1.print_description()
athlete1.change_height(72)
athlete1.print_description()
print(athlete1.get_sport())

athlete2 = Athlete(67, 150, 'basketball')
athlete2.print_description()