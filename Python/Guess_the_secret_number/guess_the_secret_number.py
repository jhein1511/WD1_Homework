secret = 25
guess = int(raw_input("Guess the secret number: "))

if secret == guess:
    print "Congratulations, you're right!"

else:
    print "Nope, that's wrong. The secret number is not" + str(guess)
