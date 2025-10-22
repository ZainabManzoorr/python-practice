num = input("Guess a number between 1 and 10: ")
import random
def check_guess(guess):
  number = random.randint(1,10)
  if guess == number:
    return "Congratulations! You guessed it right."
  else:
    return f"Sorry, the correct number was {number}. Try again!"
result = check_guess(int(num))
print(result)