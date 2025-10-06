
weight = float(input("Enter weight: "))
weight_pounds = weight * 0.45
weight_pounds = round(weight_pounds, 2)
weight_kilograms = weight * 2.2
weight_kilograms = round(weight_kilograms, 2)
question = input("(L)bs or (K)g: ")
if question == "L" or question == "l":
    print(f"You are {weight_pounds} kilograms.")
if question == "K" or question == "k":
    print(f"You are {weight_kilograms} pounds.")


