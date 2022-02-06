numbers = [1, 2, 3]
x, y, z = numbers

print(x, y, z)

customer = {
    "name": "Krishna",
    "place": "jaipur",
    "gender": "Male"
}

print(customer)

x, y, z = customer
print(x, y, z)  # returns only keys

customer["name"] = "Josh"
print(customer)


