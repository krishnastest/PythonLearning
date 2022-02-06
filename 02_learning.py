# houseprice= 1000000
# is_goodcredit = True
#
# if is_goodcredit:
#     down_payment = 0.1 * houseprice
# else:
#     down_payment = 0.2 * houseprice
# print(f'Your Down Payment is ${down_payment}')
#
# has_high_income = True
# has_good_credit = True
#
# if has_high_income and has_good_credit:
#     print("Is eligible for loan")

name = input("Enter your name \n" )
length = len(name)

if length < 3:
    print("Name must be at least 3 characters")
elif length > 50:
    print("Name can be a maximum of 50 characters")
else:
    print("Name looks good")