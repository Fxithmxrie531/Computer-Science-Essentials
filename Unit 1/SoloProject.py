print("Welcome to the all operation calculator")
operation=input("enter which operation you would like to use, +,-,*,/")
first_num=int(input("Enter first number"))
second_num=int(input("Enter second number"))
if operation== "+":
    output=(first_num+second_num)
    print(output)
elif operation== "-": 
    output=(first_num-second_num)
    print(output)  
elif operation== "*": 
    output=(first_num*second_num)
    print(output)
elif operation== "/": 
    output=(first_num/second_num)
    print(output)
else:
    print("error has occured")
