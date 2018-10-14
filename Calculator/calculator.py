x = int(raw_input("Please enter a value for x: "))
print x

y = int(raw_input("Please enter a value for y: "))
print y

operation = raw_input("Choose math operation (+, -, *, /: ")
print operation

if operation == "+":
    print x + y
elif operation == "-":
    print x - y
elif operation == "*":
    print x * y
elif operation == "/":
    print x / y
else:
    print "You need to choose a math operation. Try again!"