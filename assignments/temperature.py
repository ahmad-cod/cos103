# convert celcius to fahrenheit
# convert fahrenheit to degrees celcius
'''

1. Prompt the user to enter a temperature in degrees Fahrenheit and then display the temperature converted to Celsius
2. Prompt the user to enter a temperature in degrees Celsius and then display the temperature converted to Fahrenheit
3. Display all converted temperatures rounded to two decimal places
4. Use the following formulas to convert the temperatures:
    Celsius = (Fahrenheit - 32) * 5/9
    Fahrenheit = Celsius * 9/5 + 32
    
'''

def convert_cel_to_far(cel):
    return (cel * 9/5) + 32

def convert_far_to_cel(far):
    return (far - 32) * 5/9

print("Enter a temperature in degrees Celcius: ")
cel = float(input())

print("Enter a temperature in degrees Fahrenheit: ")
far = float(input())

cel_converted = convert_cel_to_far(cel)
far_converted = convert_far_to_cel(far)

print(f"{cel} degrees Celsius is equal to {cel_converted:.2f} degrees Fahrenheit")
print(f"{far} degrees Fahrenheit is equal to {far_converted:.2f} degrees Celsius")