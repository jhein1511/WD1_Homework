print "Hi! This is a unit converter which converts kilometers into miles."

while True:
    print "Please enter a number of kilometers you want to convert into miles. Please only use numbers."
    km = raw_input("Kilometers: ")

    try:
        km = float(km.replace(",", ".")) # changing comma to dots if necessary

        miles = km * 0.621371

        print "{} kilometers is {} miles.".format(km, miles)

    except Exception as e:
        print "Don't forget to choose a number, not text."


    sec_conversion = raw_input("Would you like to convert another time (yes, no): ")

    if sec_conversion.lower() != "yes" and sec_conversion.lower() != "y":
        break
