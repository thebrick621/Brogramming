import color
import essential
color = color.color


current_inv = []

def inv_sizecheck():
  while len(current_inv) > 10:
    current_inv.pop(10)
    print(color.BOLD + color.RED + "YOUR INVENTORY IS FULL!" + color.END)

def invcheck():
  if bool(current_inv) is False:
    print("")
    print(color.GREEN + "You have nothing in your inventory." + color.END)
  else:
    print("")
    for x in current_inv:
      print(color.BLUE + x + color.END)