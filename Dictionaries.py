numbers = {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine",
    "0" : "zero"
}
user_input = input("Phone : ")

output_string = ""

for ch in user_input:
    output_string += numbers.get(ch, "!") + " "
print(output_string)



