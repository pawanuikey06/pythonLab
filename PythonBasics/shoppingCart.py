foods=[]
prices=[]
total =0


while True:
    food =input("Enter food to buy :")
    if food.lower() =='q':
        break
    else:
        price=float(input(f"Enter Price of a {food}: $"))
        foods.append(food)
        prices.append(price)
    

print("------Your Cart-----")

for food in foods:
    print(food,end=" ")


for price in prices:
    total+=price

print()
print(f"Your Total is: ${total}")