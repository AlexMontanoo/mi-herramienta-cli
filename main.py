def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32


temperatura = float(input("Ingresa la temperatura en Celsius: "))
resultado = celsius_a_fahrenheit(temperatura)

print(f"{temperatura}°C equivalen a {resultado:.2f}°F")
