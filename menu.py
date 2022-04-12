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
        
    if len(toDelete) == 1:
      print ("Are you sure you want to delete: (Y/N)")
      toDelete[0].displayInfo()
      if input().upper() == "Y":
        toDelete[0].delete()
    else:
      for item in toDelete:
        item.displayInfo()
      print ("\nEnter the ID number of the item you would like to delete: ")
      print ("Enter -1 to cancel")
      id = int(input())
      if id == -1:
        return 0
      elif id > len(food.foods) or id < 0:
        id = int(input("That is not a valid answer, try again: "))
      else:
        item.delete()
    
    
  def option3(self): #view all eaten/calories left 
    total = func.getTotal()
    func.viewList()
    print (f"\nYour target goal is {food.targetCal} calories")
    print (f"You have eaten {total} calories so far\n")
    
  def option4(self): #change calorie goal
    food.targetCal = input("What would you like the new calorie goal to be: ")
    
  def option5(self): #clear list
    food.foods.clear()

  def showHeader(self):
    options = ["Add food", "Delete food", "View eaten today", "Change calorie goal", "Clear list"]
    for i in range(0,5):
      print (str(i+1), " ", options[i])
    print("\n\nPlease enter a number corresponding to each option from 1-5: ")

