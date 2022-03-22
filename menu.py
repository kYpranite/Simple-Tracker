import functions as func
import food

class Options:
  def doOption(self, opt):
    option = f"option{opt}"
    func = type(self).__dict__.get(option)
    if (hasattr(func,"__call__")):
      return func(self)
    raise ValueError(f'Unsupported option: {opt}')
    
class Menu(Options):
  def option1(self): #add food
    item = food.Food(input("What is the name of the food: "), 
    int(input("How many calories is the food: ")))
    item.promptUser()
    
  def option2(self): #delete food
    deleteItem = input("Enter the name of the item you would like to delete: ")
    toDelete = []
    for item in food.foods:
      if item.name.lower() == deleteItem.lower():
        toDelete.append(item)
    for item in toDelete:
      item.displayInfo
      print("\n Please enter the ID number of the item you would like to delete: ")
    
      
    
  def option3(self): #view all eaten/calories left 
    total = func.getTotal()
    func.viewList()
    print (f"\nYour target goal is {food.targetCal} calories")
    print (f"You have eaten {total} calories so far")
    
  def option4(self): #change calorie goal
    food.targetCal = input("What would you like the new calorie goal to be: ")
    
  def option5(self): #clear list
    food.foods.clear()

