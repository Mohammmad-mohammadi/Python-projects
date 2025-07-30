import random
x = random.randint(1, 100)
print("I am thinking of a number between 1 and 100. Can you guess it?")

guesses = 0  # Tracking the number of attempts

while True:
    guess = int(input("Your chosen number is: "))
    guesses += 1
    if guess > x:
        print("Too high!")
    elif guess < x:
        print("Too low!")
    else:
        print("Bingo")
        break  # Exit the loop when correct

print("Let's see how your intuition did:",guesses,"tries")

if guesses == 1:
    print("WHO GAVE YOU THE BLOODY ANSWER?!")
elif 1 < guesses < 3:
    print("Eh, not bad")
elif 3 <= guesses < 10:
    print("Nice! Not quite psychic but above average.")
elif 10 <= guesses < 20:
    print("Not a mind reader. But hey, you showed resilience—I respect that.")
else:
    print("You are statistically doing better than my grandma.")

