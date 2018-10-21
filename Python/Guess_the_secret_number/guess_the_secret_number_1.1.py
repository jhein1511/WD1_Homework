import random


def main():
    secret = random.randint(1, 51)

    while True:
        guess = int(raw_input("Guess the secret number which is between 1 and 50: "))

        if secret == guess:
            print "Congratulations, you're right!"
            break
        elif guess < secret:
            print "Sorry, your guess is too low. Try again!"
        elif guess > secret:
            print "Sorry, your guess is too high. Try again!"

if __name__ == "__main__":
    main()
