
targetCal = int(input("Enter your calorie goal: "))
foods = []

class Food():

  def __init__(self, name, calories):
    self.name = name
    self.calories = calories
    self.id = len(foods)+1

  def checkDeficit(self, extra):
    total = 0
    for food in foods:
      total += (food.calories)
    total += extra
    if total > targetCal:
      return False, targetCal-total
    elif total <= targetCal:
      return True, targetCal-total
      
  def promptUser(self):
    userInput = -1
    deficit = self.checkDeficit(self.calories)
   
    if deficit[0] == False:
      print (f"Eating this {self.name.lower()} will put you {abs(deficit[1])} calories over your daily caloric amount")
      print ("Are you sure you want to eat it anyways: (Y/N)")
      userInput = input().upper()
    else:
      print (f"After eating this {self.name.lower()}, you will have {deficit[1]} calories remaining")
      print ("Do you want to proceed with eating this food: (Y/N)")
      userInput = input().upper()
      
    if userInput == 'Y':
      self.addFood()
      
  def addFood(self):
    foods.append(Food(self.name, self.calories))
    print ("\n")

  def displayInfo(self):
    print (f"\nName: {self.name}\nCalories: {self.calories}\nID: {self.id}\n")
    
  def delete(self):
    for item in foods:
      if item == self:
        foods.remove(item)