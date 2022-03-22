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
  food.foods.remove(func.searchListById(item))

def getTotal():
  return sum(item.calories for item in food.foods)
