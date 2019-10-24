# Create Simple Calculator using Python

# Set variable for Calculation
num1 = int(input("Enter the First Number: "))
operator = (input("Enter the Operator: "))
num2 = int(input("Enter The Second Number: "))
print("Result in Below")

# Set the Operator for Operation
if operator == '+':
    result = num1 + num2
    print("{} + {} = ".format(num1, num2), result)
elif operator == '-':
    result = num1 - num2
    print("{} - {} = ".format(num1, num2), result)
elif operator == '*':
    result = num1 * num2
    print("{} * {} = ".format(num1, num2), result)
elif operator == '/':
    result = num1 / num2
    print("{} / {} = ".format(num1, num2), result)
else:
    print("Calculation Error")
