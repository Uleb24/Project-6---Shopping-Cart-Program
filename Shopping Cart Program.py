# Project 6 - Shopping Cart Program 

items = ["banana", "orange", "apple", "chips", "sour candy", "water"]
banana = 0.67
orange = 0.56
apple = 0.78
chips = 1.27
sourcandy = 1.57
water = 0.99
selection = []
prices = []

print("Welcome to Uleb Shop ! Below you can find the items we have in stock today !")
print()
print(items[0:6])
print()

while True:
    select = input("What would you like to add to the cart ? (c to go to cart)")
    selection.append(select)
    if select == "c":
        selection.remove("c")
        break
    elif select == "banana":
        print(f"The price of 1 banana today is {banana} !")
        select2 = input("Add to cart ? (yes/no)")
        if select2 == "yes":
            prices.append(banana)
            print(f"Added {select} to the cart !")
        elif select2 == "no":
            selection.remove("banana")
            print("No Worries !")
        else:
            print("Error ! Please select yes or no !")
    elif select == "orange":
        print(f"The price of 1 orange today is {orange} !")
        select2 = input("Add to cart ? (yes/no)")
        if select2 == "yes":
            prices.append(orange)
            print(f"Added {select} to the cart !")
        elif select2 == "no":
            selection.remove("orange")
            print("No Worries !")
        else:
            print("Error ! Please select yes or no !")
    elif select == "apple":
        print(f"The price of 1 apple today is {apple} !")
        select2 = input("Add to cart ? (yes/no)")
        if select2 == "yes":
            prices.append(apple)
            print(f"Added {select} to the cart !")
        elif select2 == "no":
            selection.remove("apple")
            print("No Worries !")
        else:
            print("Error ! Please select yes or no !")
    elif select == "chips":
        print(f"The price of 1 bag of chips today is {chips} !")
        select2 = input("Add to cart ? (yes/no)")
        if select2 == "yes":
            prices.append(chips)
            print(f"Added {select} to the cart !")
        elif select2 == "no":
            selection.remove("chips")
            print("No Worries !")
        else:
            print("Error ! Please select yes or no !")
    elif select == "sour candy":
        print(f"The price of 1 bag of sour candy today is {sourcandy} !")
        select2 = input("Add to cart ? (yes/no)")
        if select2 == "yes":
            prices.append(sourcandy)
            print(f"Added {select} to the cart !")
        elif select2 == "no":
            selection.remove("sour candy")
            print("No Worries !")
        else:
            print("Error ! Please select yes or no !")
    elif select == "water":
        print(f"The price of 1 bo'oh'oh'wo'ah today is {water} !")
        select2 = input("Add to cart ? (yes/no)")
        if select2 == "yes":
            prices.append(water)
            print(f"Added {select} to the cart !")
        elif select2 == "no":
            selection.remove("water")
            print("No Worries !")
        else:
            print("Error ! Please select yes or no !")
    else:
        selection.remove(select)
        print("ERROR ! Invalid Item")
        print(items[0:6])
        print()

total = sum(prices)

print("----- YOUR CART -----")

for select in selection:
    print(select)

print()
print(f"Your total is: ${total:.02f} !")
print()
print("Check out ?")