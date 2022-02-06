numbers = [2,4,6,7,2,9,10]

#my code
for number in numbers:
    get_count = numbers.count(number)
    if get_count > 1:
        get_index = numbers.index(number)
        numbers.pop(get_index)
print(numbers)

uniques = []

#Mosh Code
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
