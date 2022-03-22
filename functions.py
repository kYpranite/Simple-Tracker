import food
import func

def viewList():
  print ("Foods Eaten: ")
  for item in food.foods:
    item.displayInfo()

def searchListById(id):
  for item in food.foods:
    if item.id == id:
      return item

def deleteItem(item):
  toDelete = []
  for item in food.foods:
    if item.name.lower() == deleteItem.lower():
      toDelete.append(item)
      
  if len(toDelete) == 1:
    print ("Are you sure you want to delete: (Y/N)")
    toDelete[0].displayInfo()
    if input() == "Y":
      food.foods.remove(toDelete[0])
  else:
    for item in toDelete:
      item.displayInfo()
    print ("\nEnter the ID number of the item you would like to delete: ")
    print ("Enter -1 to cancel")
    id = int(input())
    if id < len(food.foods) and id != -1:
      id = int(input("That is not a valid answer, try again: "))
    elif id == -1:
      return 0
    else:
      food.foods.remove(func.searchListById(id))

def getTotal():
  return sum(item.calories for item in food.foods)
