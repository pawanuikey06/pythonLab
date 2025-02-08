menu = {"pizza": 3.00,
               "nachos": 4.50,
               "popcorn": 6.00,
               "fries": 2.50,
               "chips": 1.00,
               "pretzel": 3.50,
               "soda": 3.00,
               "lemonade": 4.25}

cart =[]
total =0
print("---------MENU--------")
for key ,value in menu.items():
    print(f"{key:10} :${value:.2f}")

print("-------------------------")


while True:
    food=input("Select an item :").lower()
    if food.lower()=='q':
        break
    elif  menu.get(food) is not None:
        cart.append(food)
        total+=menu[food]
    else:
        print("Food is not in Menu Select another")


print("------Your Order List-------")
for item in cart:
    print(item,end=" ")

print()
print(f" Your Total bill is :${total}")


