import food

def viewList():
  print ("Foods eaten: ")
  for item in food.foods:
    item.displayInfo()

def getTotal():
  return sum(item.calories for item in food.foods)
