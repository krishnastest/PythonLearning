weight = int(input("Enter your weight \n"))
unit = input("(L)bs or (K)g : ")
if unit.lower() == 'l':
    new_weight = weight * 0.45
    print("You are " + str(new_weight) + " kilograms")
else:
    new_weight = weight // 0.45
    print(f"You are {new_weight} pounds")
