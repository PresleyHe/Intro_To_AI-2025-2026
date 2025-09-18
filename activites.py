# Classroom Practice Activities: Introduction to Algorithms with Python

# Activity 1: Step-by-Step Algorithm (Sequencing Practice)
# Task for Students:
# Write a Python algorithm that prints the steps for brushing your teeth. Include at least 4 steps.

print("First get the brush and toothpaste")
print("put the toothpaste on the toothbrush")
print("use the brush to brush your teeth")
print("Then brush it without toothpaste")



# Activity 2: Interactive Greeting (Input Practice)
# Task for Students:
# Write a Python program that:
# Asks the user for their favorite color.
# Prints: "Wow, I like [color] too!"

favorite_color = input("Favorite Color:")

print(f"Wow, I like {favorite_color} too!")

# Activity 3: Number Checker (Conditionals Practice)
# Task for Students:
# Write a Python algorithm that asks the user for a number.
# If the number is positive, print "Positive number."
# If the number is zero, print "Zero."
# Otherwise, print "Negative number."

num = int(input("Number:"))

if (num % 2) == 0:
    print("Number is even")
elif num == 0:
    print("Number is 0")
else:
    print("Number is odd")
    

# Activity 4: Simple Loop (Repetition Practice)
# Task for Students:
# Write a Python algorithm that prints your name 3 times using a loop.

# Activity 5: Mini Challenge – Even or Odd Game
# Task for Students:
# Ask the user for a number.
# Print whether the number is even or odd.

number = int(input("Number:"))

if (number % 2) == 0:
    print("Number is even")
else:
    print("Number is odd")

# Activity 6: Multiplication Table Generator
# Task for Students:
# Ask the user for a number. Print its multiplication table up to 10 (example: if the input is 3 → print 3 × 1 through 3 × 10).

first_num = int(input("Number-1:"))
sec_num = int(input("Number-2:"))

print(f"{first_num} × {sec_num} --> {first_num * sec_num}")


# Activity 7: Decision Path – Movie Ticket Price
# Task for Students:
# Ask the user for their age.
# If under 13 → print "Child ticket: $8"
# If between 13 and 59 → print "Adult ticket: $12"
# If 60 or older → print "Senior ticket: $6"

Student_age = int(input("What is your age:"))

if Student_age < 13:
    print("Child ticket: $8")
elif 13 <= Student_age <= 59:
    print("Adult ticket: $12")
else:
    print("Senior ticket: $6") 