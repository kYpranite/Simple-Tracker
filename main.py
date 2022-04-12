import menu as m


if __name__ == "__main__":
  menu = m.Menu()
  while True:
    menu.showHeader()
    menu.doOption(input())
    print("---------------")
    print("\n")
