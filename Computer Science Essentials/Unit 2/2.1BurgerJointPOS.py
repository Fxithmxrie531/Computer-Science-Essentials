
#BROWNTOWN BURGER JOINT POINT OF SALE SOFTWARE
#VERSION 1.21 LAST REVISION DATE 3/11/2024


#VARIABLES
orderComplete = False
totalCost = 0
tax = 0.06

#WELCOME THE USER TO THE POINT OF SALE(POS)
print()
print()
print("Welcome to the Browntown Burger Joint, voted 2nd best Burger in Browntown")
print()

#ASK THEM FOR THEIR NAME AND STORE IT IN name
name = input("Can I have your name please?  ")
print()
print("Thanks " + name)
print()
print()


#POINT OF SALE LOOP
while orderComplete == False:
    #STAY IN THIS LOOP UNTIL THEY SELECT "COMPLETE ORDER"
    print()
    print ("What would you like to order: Burgers, Sides, Drinks, Complete Order.")
    menu = input("-> ")
    
    
    if menu == "Burgers":
        #IF THEY WANT TO ADD A BURGER:
        print("We offer the following burgers:")
        print("1: Hamburger $5.50")
        print("2: Cheesebuger $6.00")
        print("3: Western burger (Cheese, onion, western sauce) $6.75")
        print("4: Double Cheese Burger (2 burger patties, extra cheese, any choice of sauce) $7.99")
        burgerChoice = input("What would y ou like (input a number 1-4): ")
       
        #BURGER 1: HAMBURGER
        if burgerChoice == "1":
            totalCost = totalCost + 5.50
            print("You added Hamburger to your order")
            print("Your total cost so far: $", totalCost)

        #BURGER 2: CHEESEBURGER
        elif burgerChoice == "2":
            totalCost = totalCost + 6.00
            print("You added Cheeseburger to your order")
            print("Your total cost so far: $", totalCost)

        #BURGER 3: WESTERN BURGER
        elif burgerChoice == "3":
            totalCost = totalCost+ 6.75
            print("You added Western Burger to your order")
            print("Your total cost so far: $", totalCost)
        
        #BURGER 4: ADD ONE HERE
            #ADD A NEW BURGER OPTION AND UPDATE ALL CODE ABOVE TO MAKE IT WORK
        elif burgerChoice == "4":
            totalCost = totalCost+ 7.99
            print("You added Double Cheese Burger to your order")
            print("Your total cost so far: $", totalCost)

            
        #IF THEY GET HERE, THEY DID NOT MAKE A VALID SELECTION
        else:
            print("please make a valid choice")
        
    elif menu == "Sides":
        print("We offer the following sides:")
        print("1: PLAIN fries $3.25")
        print("2: Chilly Cheees fries $5.45")
        print("3: Crispy onion rings $6.45")
        print("4: Fresh hot mozzerella sticks $6.45")
        sideChoice = input("What would you like (input a number 1-4): ")
        
         #SIDE 1: PLAIN FRIES
        if sideChoice == "1":
            totalCost = totalCost + 3.25
            print("You added plainfries to your order")
            print("Your total cost so far: $", totalCost)

             #SIDE 2: CHILLY CHEESE FRIES
        if sideChoice == "2":
            totalCost = totalCost + 5.45
            print("You added chilly cheese fries to your order")
            print("Your total cost so far: $", totalCost)

             #SIDE 3: CRISPY ONION RINGS 
        if sideChoice == "3":
            totalCost = totalCost + 6.45
            print("You added crispy onion rings to your order")
            print("Your total cost so far: $", totalCost)
            
             #SIDE 4: FRESH HOT MOZZERELLA STICKS
        if sideChoice == "4":
            totalCost = totalCost + 6.45
            print("You added fresh hot mozzerella sticks to your order")
            print("Your total cost so far: $", totalCost)

    elif menu == "Drinks":
        print("We offer the following drinks:")
        print("1: Gatorade $2.75")
        print("2: Coca-cola $3.25")
        print("3: Dr.Pepper $3.25")
        print("4: Bottled Water $1.75")
        drinkChoice = input("What would you like (input a number 1-4): ")

         #DRINK 1: GATORADE
        if drinkChoice == "1":
            totalCost = totalCost + 2.75
            print("You added gatorade to your order")
            print("Your total cost so far: $", totalCost)

        #DRINK 2: COCA-COLA
        if drinkChoice == "2":
            totalCost = totalCost + 3.25
            print("You added coca-cola to your order")
            print("Your total cost so far: $", totalCost)

        #DRINK 3: DR.PEPPER
        if drinkChoice == "3":
            totalCost = totalCost + 3.25
            print("You added dr.pepper to your order")
            print("Your total cost so far: $", totalCost)

        #DRINK 4: BOTTLED WATER
        if drinkChoice == "4":
            totalCost = totalCost + 1.75
            print("You added bottled water to your order")
            print("Your total cost so far: $", totalCost)

    
    
    elif menu == "Complete Order":
        #IF THEY SELECT COMPLETE ORDER, SET THE ORDERCOMPLETE TO TRUE
        orderComplete = True
        print()

        #GIVE THEM THEIR TOTALS
        #Finish this section to give you a grand total as well as print your complete order
        print("order finished")
        print("You have ordered")
        print("Subtotal: $", totalCost)
        totalTax = float(totalCost) * tax
        print("Total Tax: $", totalTax)
        totalCost+=totalTax 
        print("Grand Total: $",totalCost)

        
 
        
    else:
        print("Sorry, not a valid choice, please start over...")

#THE USER ONLY GETS HERE IF THEY FINISH THEIR ORDER
print("Thank you for eating with us!")
