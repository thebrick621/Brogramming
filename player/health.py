import color
color = color.color

ur_health = 100.00

def ur_ded():
  if ur_health <= 10.00:
    print(color.RED + color.BLINK + "LOW HEALTH!!!" + color.END)
  if ur_health <= 0.00:
    print(color.RED + color.BOLD + "You died. Please restart." + color.END)