#MATH GAME BY LOKESH
import random

print("Welcome to the math horror game")
input("Press Enter to start")

print("Your game starts now.........................")

arithmetic = ['+', '-', '*']

points = 0  # Move point initialization outside of the loop

while True:
    random_a = random.randint(0, 9)
    random_b = random.randint(0, 9)
    random_s = random.choice(arithmetic)

    # Calculate correct answers for each operation
    ans_a = random_a + random_b
    ans_s = random_a - random_b
    ans_m = random_a * random_b

    # Use the correct operation based on random_s
    if random_s == "+":
        correct_answer = ans_a
    elif random_s == "-":
        correct_answer = ans_s
    else:
        correct_answer = ans_m

    # Fix the print statement, don't use print as a variable name
    user_input = int(input(f"{random_a} {random_s} {random_b} = "))

    if user_input == correct_answer:
        points += 1
        print(f"Correct! Your points: {points}")
    else:
        print(f"Wrong! Your points: {points}")
        exit('Game Over')


