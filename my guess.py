import random

best_score=0

def play_game():

 print("Welcome To Number Guessing Game")

 while True:
  lrange=int(input("Please enter a number for lower range"))
  urange=int(input("Please enter a number for upper range"))

  if urange<lrange or urange==lrange:
     print("Upper range number cannot be smaller or equal to the lower range number")
     continue
  else:
      secret_num = random.randint(lrange, urange)
      break

 attempts=0
 while True:
    num=int(input(f"Please enter a number between your range {lrange} to {urange}"))

    if num>urange or num<lrange:
        print("Number not in the specific range provided Please provide number within the range")
        continue

    attempts = attempts + 1

    if secret_num==num:
        print("you won guessed the correct number")
        print("you took",attempts,"numbers of attempts")
        return attempts
    elif num>secret_num:
     print("Number is too high try again!!")
    else:
     print("Number is too low try again!!")


while True:
    current_score=play_game()
    if best_score==0 or current_score<=best_score:
        best_score=current_score
        print(f"Your Best Score is {best_score}")
    else:
        print(f"Your Best Score is {best_score}")
    again=input("Do you want to play again type yes/no:").lower()
    if again!="yes":
     print("Thanks for playing")
     break