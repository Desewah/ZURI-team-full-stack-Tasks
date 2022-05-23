#Operations include addition, subtraction, multiplication, division and modulus operations
print("Select an operation to perform.")
print("1. Addition ")
print("2. Subtraction ")
print("3. Multiplication ")
print("4. Division ")
print("5. Modulus ")
#Ask user for the operation to be carried out.
operation = input("What operation do you want to perform? ")
if operation == "1":
    num1 = int(input("What's num 1? "))
    num2 = int(input("What's num2? "))
    print("The sum is " + str(num1+num2))
elif operation == "2":
    num1 = int(input("What's num 1? "))
    num2 = int(input("What's num2? ")) 
    print("The subtraction is " + str(num1-num2))  
elif operation == "3":
    num1 = int(input("What's num 1? "))
    num2 = int(input("What's num2? ")) 
    print("The multiplication is " + str(num1*num2))
elif operation == "4":
    num1 = int(input("What's num 1? "))
    num2 = int(input("What's num2? "))
    print("The division is " + str(num1/num2))
elif operation == "5":
    num1 = int(input("What's num 1? "))
    num2 = int(input("What's num2? "))
    print("The modulus is " + str(num1%num2))
else:
    print("Invalid entry. ")