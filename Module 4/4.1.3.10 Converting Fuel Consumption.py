def litres_100km_to_miles_gallon(litres):
    gallons = litres / 3.78
    miles = 100 * 1000 / 1609.344
    return miles/gallons


def miles_gallon_to_liters_100km(miles):
    km100 = miles * 1609.344 / 1000/ 100
    litres = 3.785411784
    return litres / km100


print(litres_100km_to_miles_gallon(3.9))
print(litres_100km_to_miles_gallon(7.5))
print(litres_100km_to_miles_gallon(10.))
print(litres_100km_to_miles_gallon(60.3))
print(litres_100km_to_miles_gallon(31.4))
print(litres_100km_to_miles_gallon(23.5))
