num1 = float(input("Enter a number: "))

print ("Available operations: ","+","-","*","/","**","//",sep=" ")

arithmeticOperations = input("Enter an arithmetic operation: ")
8
num2 = float(input("Enter another number: "))







if arithmeticOperations == '+':
    print(num1 + num2)
elif arithmeticOperations == '-':
    print(num1 - num2)
elif arithmeticOperations == '*':
    print(num1 * num2)
elif arithmeticOperations == '/':
    print(num1 / num2)
elif arithmeticOperations == '//':
    print(num1 // num2)
elif arithmeticOperations == '**':
    print(num1 ** num2)

