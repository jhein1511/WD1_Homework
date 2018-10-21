# coding=utf-8
import json

menu = {}

while True:

    answer = raw_input("Would you like to insert a dish? (y/n)\n")
    if answer.lower().strip() != "y":
        break

    dish = raw_input("Please enter the name of your dish:\n")
    while True:
        price = raw_input("Please enter the price of {}:\n".format(dish))
        try:
            price = float(price)
            break
        except:
            continue

    menu[dish] = price

average_price = sum(menu.values()) / len(menu.values())
print("Calculating average price: {}".format(average_price))

with open("menu.json", "w") as f_out:
    json.dump(menu, f_out)

with open("menu.txt", "w") as f_out:
    for dish, price in menu.items():
        text = "{}: {} €\n".format(dish, price)
        print(text)
        f_out.write(text)
