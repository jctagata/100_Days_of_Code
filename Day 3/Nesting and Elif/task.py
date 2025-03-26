# Get Math Grade

math_grade = int(input("What was your grade in Math?: "))
eng_grade = int(input("What was your grade in English?: "))

if math_grade >= 90:
    if eng_grade >= 90:
        print(f"Woah, you're good at both Math and English!")
    else:
        print(f"You're good at Math!")
elif eng_grade >= 90:
    print(f"You're good at English!")
else:
    print("Hey, it doesn't matter. Study harder!")
