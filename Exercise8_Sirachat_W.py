usernameInput = input("Username : ")
passwordInput = input("Password : ")

if usernameInput == "test" and passwordInput == "223" :
    print ("Login success!")
    print ("*-- Snack Shop --*")
    print ("1. Banana    : Price 20 THB")
    print ("2. Chocolate : Price 18 THB")
    print ("3. Boba      : Price 32 THB")

    itemSelected = int(input("Select the number do you need : "))
    if itemSelected == 1:
        Banana = 20
        amountBanana = int(input("Amount: "))
        print ("Total price = ",Banana*amountBanana," THB")
    elif itemSelected == 2:
        Chocolate = 18
        amountChocolate = int(input("Amount: "))
        print ("Total price = ",Chocolate*amountChocolate," THB")
    elif itemSelected == 3:
        Boba = 32
        amountBoba = int(input("Amount: "))
        print = ("Total price = ", Boba * amountBoba, " THB")
    else:
        print("Invalid please login to try select again")

else:
    print ("Wrong username or password please try again")