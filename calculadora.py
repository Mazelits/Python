def calculadora():
    print("Calculadora básica")
    print("Ingrese la operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    opcion = input("Seleccione el número de la operación deseada: ")

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if opcion == '1':
        print("Resultado:", num1 + num2)
    elif opcion == '2':
        print("Resultado:", num1 - num2)
    elif opcion == '3':
        print("Resultado:", num1 * num2)
    elif opcion == '4':
        if num2 != 0:
            print("Resultado:", num1 / num2)
        else:
            print("Error: división por cero")
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

# Llamar a la función calculadora para comenzar el programa
calculadora()
