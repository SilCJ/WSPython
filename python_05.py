def suma (num_1: int , num_2: int):
    print(f"Sumar los numeros: {num_1} + {num_2}")
    return num_1 + num_2

numero_1 = input("Numero A:")
numero_2 = input("Numero B:")
numero_1 = int(numero_1)
numero_2 = int(numero_2)

print(f"El resultado de la suma es: {suma (numero_1, numero_2)}")


def resta  (num_3: int , num_4: int):
    print(f"Restar los numeros: {num_3} - {num_4}")
    return num_3 - num_4

numero_3 = input("Numero A:")
numero_4 = input("Numero B:")
numero_3 = int(numero_3)
numero_4 = int(numero_4)

print(f"El resultado de la resta es: {resta (numero_3, numero_4)}")


def multiplicacion  (num_5: int , num_6: int):
    print(f"Multiplicar los numeros: {num_5} * {num_6}")
    return num_5 * num_6

numero_5 = input("Numero A:")
numero_6 = input("Numero B:")
numero_5 = int(numero_5)
numero_6 = int(numero_6)

print(f"El resultado de la multiplicación es: {multiplicacion (numero_5, numero_6)}")


def division  (num_7: int , num_8: int):
    print(f"Dividir los numeros: {num_7} / {num_8}")
    return num_7 / num_8

numero_7 = input("Numero A:")
numero_8 = input("Numero B:")
numero_7 = int(numero_7)
numero_8 = int(numero_8)

print(f"El resultado de la división es: {division (numero_7, numero_8)}")

def conversion(var):
    print(f"Captura un número entero: {var}")
    return var

numero_9 = input("Número entero:")
numero_9 = float(numero_9)

print(f"La conversión de entero a flotante es: {numero_9}")

def modulo(num_10: int , num_11: int):
    print(f"Captura el número a y b es: {num_10} {num_11}")
    return numero_10, numero_11

numero_10 = input("Número entero A:")
numero_11 = input("Número entero B:")
numero_10 = int(numero_10)
numero_11 = int(numero_11)


print(f"El resultado del módulo es: {modulo(numero_10, numero_11)}")








