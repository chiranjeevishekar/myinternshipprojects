def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

try:
    celsius = float(input("Enter temperature in Celsius: "))

    fahrenheit = celsius_to_fahrenheit(celsius)

    print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit")

except ValueError:
    print("Invalid input. Please enter a valid number for Celsius temperature.")
