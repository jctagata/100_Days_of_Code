print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

total_cost = int(0)

if size == "S":
    total_cost += 15

    if pepperoni == "Y":
        total_cost += 2
    else:
        ...

    # Extra Cheese
    if extra_cheese == "Y":
        total_cost += 1
    else:
        ...

elif size == "M":
    total_cost += 20

    # Extra Pepperoni
    if pepperoni == "Y":
        total_cost += 3
    else:
        ...
    # Extra Cheese
    if extra_cheese == "Y":
        total_cost += 1
    else:
        ...
elif size == "L":
    total_cost += 25

    # Extra Pepperoni
    if pepperoni == "Y":
        total_cost += 3
    else:
        ...

    # Extra Cheese
    if extra_cheese == "Y":
        total_cost += 1
    else:
        ...

else:
    print("Sorry, I didn't understand that")

print(f"The total cost of your pizza is ${total_cost}")
