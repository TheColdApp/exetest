import random

def guess_the_number():
    number = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100.")
    
    while True:
        try:
            guess = int(input("Take a guess: "))
            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print("Congratulations! You guessed it!")
                break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    guess_the_number()
