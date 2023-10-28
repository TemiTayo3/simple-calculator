name = input('Please enter your name ')
val1 = input('Please enter first number ')
user = input('Please enter your operation (+, -, / or *) ')
# operator = ['+' , "-", "/", "*"]
val2 = input('Please enter second number ')
addition = float(val1) + float(val2)
subtraction = float(val1) - float(val2)
division = float(val1) / float(val2)
multiplication = float(val1) * float(val2)

if user == '+':
    print('HELLO '+ name + ' the result is ' + str(addition) )

elif user == '-':
    print('HELLO '+ name + ' the result is ' + str(subtraction) )

elif user == '/':
    print('HELLO '+ name + ' the result is ' + str(division) )

elif user == '*':
    print('HELLO '+ name + ' the result is ' + str(multiplication) )

else:
    print("Please note you must enter either +, -, / or *")


# meat = input("What meat is available >")
# if meat == "egg" or meat == "fish":
#     print("I will buy meat")
# else:
#     print("I will not buy anything.")