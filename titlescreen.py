import color
color = color.color

def title():
  print(color.BOLD + color.GREEN + "			  ,---------------------------,")
  print("              |  /---------------------\  | ")
  print("              | |                       | | ")
  print("              | |                       | | ")
  print("              | |    C:>BROGRAMMING_    | | ")
  print("              | |                       | | ")
  print("              | |                       | | ")
  print("              |  \_____________________/  | ")
  print("              |___________________________| ")
  print("            ,---\_____     []     _______/------, ")
  print("          /         /______________\           /| ")
  print("        /___________________________________ /  | ___ ")
  print("        |                                   |   |    ) ")
  print("        |  _ _ _                 [-------]  |   |   ( ")
  print("        |  o o o                 [-------]  |  /    _)_ ")
  print("        |__________________________________ |/     /  / ")
  print("    /-------------------------------------/|      /__/ ")
  print("  /-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ / ")
  print("/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ / ")
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")
  
def ask():
  s = input(color.END + color.BOLD + "          Would you like to play? " + color.GREEN + "[Y] " + color.END + "or " + color.BOLD + color.YELLOW + "[N]\n" + color.END)
  print ("")
  return s
  
def start_game():
  yorn = ask()
  yorn = yorn.upper()
  if yorn == str("N"):
      print(color.BOLD + color.YELLOW + "BYE BYE!")
      quit()
  while yorn != str("Y"):
    yorn = ask()
    yorn = yorn.upper()
  if yorn == str("Y"):
      print(color.RED + color.BOLD + "LETS BEGIN!" + color.END)
      print("")
      print(color.GREEN + "You were asleep. You open your eyes and appear to be in a room. It's familiar.\n" + color.END)