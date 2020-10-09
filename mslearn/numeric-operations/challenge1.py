fahrenheit = input('What is the temperature in fahrenheit? ')
if fahrenheit.isnumeric() == False :
    print('Input is not a number.')
    exit()
else :
    celcius = (float(fahrenheit) - 32) * 5/9
    print('Temperature in celcius is ' + str(round(celcius,2)))


