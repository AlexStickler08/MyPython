while True:
    print("[1] add [2] subtract [3] multiply [4] divide")
    calculation = input("Please pick a type of calculation: ")
    
    if calculation == "1":
        add1 = input("What number would you like to add to: ")
        add2 = input("What number would you like to add with: ")
        print(int(add1) + int(add2))
    
    elif calculation == "2":
        subtract1 = input("What number would you like to subtract to: ")
        subtract2 = input("What number would you like to subtract with: ")
        print(int(subtract1) - int(subtract2))
    
    elif calculation == "3":
        multiply1 = input("What number would you like to multiply: ")
        multiply2 = input("What number would you like to multiply with: ")
        print(int(multiply1) * int(multiply2))
    
    elif calculation == "4":
        divide1 = input("What number would you like to divide: ")
        divide2 = input("What number would you like to divide with:")
        print(int(divide1) / int(divide2))
        
    else:
        print("Please pick between [1]adding or [2]subtracting!")
        
    another_calculation = input("Would you like to perform another calculation? [Y/n]: ")
    if another_calculation.lower() != "y":
        break

print("done!")

    


    






