student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

## Summation
# Auto
total_score = sum(student_scores)

print(total_score)

# Manual
sum = 0
for score in student_scores:
    sum += score

print(sum)

# Highest Score
# Auto
highest = max(student_scores)
print(highest)

## Challenge
# You are given a list of exam scores, and you have to print out the highest score from the List.
# You will need to use what you have learnt about Lists, For Loops and Conditionals to print out
# the highest score in the list of student_scores. For example, if the scores were:

test_scores = [8, 65, 89, 86, 55, 91, 64, 89]
highest = 0
for test in test_scores:
    if test > highest:
        highest = test

print(highest)