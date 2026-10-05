def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def millas_a_kilometros(millas):
    return millas * 1.60934


print("Seleccione una opción:")
print("1. Celsius a Fahrenheit")
print("2. Millas a Kilómetros")

opcion = input("Opción: ")

if opcion == "1":
    temperatura = float(input("Ingresa la temperatura en Celsius: "))
    resultado = celsius_a_fahrenheit(temperatura)
    print(f"{temperatura}°C equivalen a {resultado:.2f}°F")

elif opcion == "2":
    millas = float(input("Ingresa la distancia en millas karnalaso "))
    kilometros = millas_a_kilometros(millas)
    print(f"{millas} millas equivalen a {kilometros:.2f} km")

else:
    print("Opción no válida")
