def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def millas_a_kilometros(millas):
    return millas * 1.60934


temperatura = float(input("Ingresa la temperatura en Celsius: "))
resultado = celsius_a_fahrenheit(temperatura)

print(f"{temperatura}°C equivalen a {resultado:.2f}°F")

millas = float(input("Ingresa la distancia en millas karnal "))
kilometros = millas_a_kilometros(millas)

print(f"{millas} millas equivalen a {kilometros:.2f} km")
`
