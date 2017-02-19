menu = {}

while True:
    name = raw_input("Vpisi ime jedi: ")
    price = raw_input("Vpisi ceno jedi: ")

    menu[name] = price

    if raw_input("Zelite dodati se eno jed?(da/ne): ") == "ne":
        break

print ("Menu: %s" % menu)

daily_menu = open("menu.txt", "w+")
for dish in menu:
    daily_menu.write("%s, %s \n" % (dish, menu[dish]))

daily_menu.close()