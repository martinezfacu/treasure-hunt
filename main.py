print("             |")
print("             |")
print("           |-|-|      ")
print("             |         ")
print("             |      ")
print("          '--|      ")
print("            .|]_   ")
print("      _.-=.' |     | ")
print("      |    |  |]_   | ")
print("      |_.-='  |   __|__ ")
print("       _.-='  |\   /|\ ")
print("      |    |  |-'-'-'-'-. ")
print("      |_.-='  '=========' ")
print("           `   |     | ")
print("            `. |    / \ ")
print("             ||   /   \____.--=''''==--.._")
print("              ||_.'--=='    |__  __  __  _.' ")
print("              ||  |    |    |\ ||  ||  || |                        ___")
print(" ____         ||__|____|____| \||__||__||_/    __________________/|   |")
print("|    |______  |===.---. .---.========''''=-._ |     |     |     / |   |")
print("|    ||     |\| |||   | |   |      '===' ||  \|_____|_____|____/__|___|")
print("|-.._||_____|_\___'---' '---'______....---===''======//=//////========|")
print("|--------------\------------------/-----------------//-//////---------/")
print("|               \                /                 // //////         /")
print("|                \______________/                 // //////         / ")
print("|                                        _____===//=//////=========/")
print("|=============================================================FACU/")
print("'----------------------------------------------------------------`\n")

print("Welcome to Treasure Island. :D")
print("Your mission is to find the treasure $. \n")

direction = input("Do you want to go left or right? Left or Right. \n")
if direction == "Left":
    swim_or_boat = input("Do you want to wait for a boat or swim? Wait or Swim. \n")
    if swim_or_boat == "Wait":
        door = input("What doors do you want to enter? Red, Blue or Yellow. \n")
        if door == "Yellow":
            print("You have won, you are the best!! :D")
        elif door == "Red":
            print("You were burned by fire! Sorry friend, you were close D: ")
        else:
            print("You have been eaten by piranhas D: ")
    else:
        print("Attacked by a shark. Game over! D:")
else:
    print("Fall into a hole. GAME OVER! D: ")
