"""
 CASE SENSITIVE
"""


def find_price(name):
    pets = {"Dog": 300, "Cat": 200}
    # p = pets.keys()
    if name in pets:
        print "price of the " + name + " is: " + str(pets[name])
    else:
        menu()


def menu():
    pet_name = raw_input("Enter a pet you want to buy: ")
    find_price(pet_name)


menu()
