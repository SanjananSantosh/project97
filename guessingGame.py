import os 
import shutil
import random

number = random.randint(1,9)
chances=0
print("guess a number between 1 and 9:")

while chances<5:
   guess = int(input("enter your guess: "))

   if guess == number:
        print("Congratulations you  won !!!!")
        break
   elif guess < number:
        print("Your guess is low , guess a number higher than", guess)
   else:
        print("Your guess is high , guess a number less than" , guess)

   chances += 1

if not chances<5:
     print("You loose! The number was",number)
