print("Welcome")
name = input("What is your name? :")
verified_names = ["Izyan", "Aiza", "Chachu"]
while name not in verified_names:
    print("Invalid name please try again")
    name = input("What is your name? :")
print("Welcome back")
print("Guess a color given below")
color = ["Blue", "Red", "Green", "Silver"]
for i in range(len(color)):
    print(i + 1, color[i])
import random
guess = input("Guess the color :")
result = random.choice(color)
if guess == random:
    print("Thats correct")
else:
    print("Thats incorrect")
    print(f"The color was {result}")    