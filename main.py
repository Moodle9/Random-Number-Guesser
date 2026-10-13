import random
import time
print("Super Cool Guessing Game :3 It's somewhere between 1 and 1000")
time.sleep(2)
print("Finding number")
time.sleep(1)
guess = int(input("What is your guess?  "))
correct_number = random.randint(1,1000)
guess_count = 1
pause_time = round(random.uniform(.5,1), 3)
while guess != correct_number:
    time.sleep(pause_time)
    guess_count += 1
    if guess < correct_number:
        print(f"Your last guess was {guess}.")
        time.sleep(pause_time)
        guess = int(input("Guess Higher Twin:  "))
    else:
        print(f"Your last guess was {guess}.")
        time.sleep(pause_time)
        guess = int(input("Guess Lower Twin:  "))

time.sleep(pause_time)
print("...")
time.sleep(pause_time)
print("H-How...")
time.sleep(pause_time)
print(f"YOUR A GOD!! HOW DID YOU GET THAT!? IN ONLY {guess_count} GUESSES TOO??")