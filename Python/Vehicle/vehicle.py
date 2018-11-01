class Vehicle(object):
    def __init__(self, brand, model, kilometers_now, service_date):
        self.brand = brand
        self.model = model
        self.kilometers_now = kilometers_now
        self.service_daten = service_date

def list_all_vehicles(vehicles):
        for index, car in enumerate(vehicles):
            print car.brand
            print car.model
            print ""  # empty line


        if not vehicles:
            print "sorry, this vehicle is not listed yet."

def add_new_vehicle(vehicles):
    brand = raw_input("Please enter the brand of the vehicle: ")
    model = raw_input("Please enter the model of the vehicle: ")
    kilometers_now = raw_input("Please enter the amount of kilometers the vehicle has done so far (please add only a nummber): ")
    service_date = raw_input("Please enter the last service date: ")

    result = new_vehicle(brand, model, kilometers_now, service_date)
    vehicles.append(result)

    print ""  # empty line
    print "You have successfully added a new vehicle: %s %s" % (brand, model)
