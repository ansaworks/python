print('Simple Calculator')
print('=================')
first_value = input('First number? ')
operation = input('Operation? ')
second_value = input('Second number? ')
if first_value.isnumeric() == False or second_value.isnumeric() == False :
    print('Please input a number.')
    exit()
else :
    first_value = int(first_value)
    second_value = int(second_value)
if operation == '+' :
    result = first_value + second_value    
elif operation == '-' :
    result = first_value - second_value
elif operation == '*' :
    result = first_value * second_value
elif operation == '/' :
    result = first_value / second_value
elif operation == '%' :
    result = first_value % second_value
elif operation == '**' :
    result = first_value ** second_value
else :
    print('Operation not recognized.')
    exit()

print(f'Product of {first_value} {operation} {second_value} equals {result}')  

