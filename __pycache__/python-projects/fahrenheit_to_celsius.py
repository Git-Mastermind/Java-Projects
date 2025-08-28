def farenheit_to_celsius(degree):
    converted_celsius = print((degree - 32) * 5/9)
    return converted_celsius

def celsius_to_farenheit(degree):
    converted_farenheit = print((degree * 9/5) + 32)
    return converted_farenheit

temperature_input = int(input('Enter a temperature: '))
conversion_input = input('(F)arenheit or (C)elsius: ').lower()
if conversion_input == 'f':
    farenheit_to_celsius(temperature_input)

elif conversion_input == 'c':
    celsius_to_farenheit(temperature_input)

else:
    print('Invalid Input!')
    
