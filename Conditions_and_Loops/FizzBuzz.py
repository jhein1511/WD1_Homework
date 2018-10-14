print "Welcome! Let's play FizzBuzz!"

user = raw_input("Select a number between 0 and 100: ")

try:
    user = int(user) # to convert the users string-number to a number (integer)

    for number in range(1, user+1):
        if number % 3 == 0 and number % 5 == 0:
            print "FizzBuzz"

        elif number % 3 == 0:
            print "Fizz"

        elif number % 5 == 0:
            print "Buzz"

        else:
            print number

except Exception as e: # to handle errors automatically
    print "You need to choose a whole number, decimal digits are not allowed."
