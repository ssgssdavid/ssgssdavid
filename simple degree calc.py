# simple degree calc

unit = input ("What temp would you like to convert, celsius or Fahrenheit (C/F ):")
temp = float(input("Enter temperature: "))

   
x = ['C', 'c','Celsius', 'celsius']
y = ['F', 'f', 'Fahrenheit' 'fahrenheit']


if unit in x:
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp}°F")

elif unit in y:
    temp = round((temp-32) * 5 / 9, 1)
    print(f"The temperature in Celsius is: {temp}°C")
else:
    print(f"{unit} is an invalid unit of measurement")
    