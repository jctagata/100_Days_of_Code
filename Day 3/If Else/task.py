print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

MIN_HEIGHT = 165

if height >= MIN_HEIGHT:
    print("Enjoy the ride!")
else:
    print("Sorry, you are too short for this ride")
