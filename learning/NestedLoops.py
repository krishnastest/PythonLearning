numbers = [5,2,5,2,2]

for number in numbers:
    x = 'x' * number
    print(x)

for number in numbers:
    output = ''
    for count in range(number):
        output += 'x'
    print(output)