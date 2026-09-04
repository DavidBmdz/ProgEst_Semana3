#Sumar dos números

def sumar(num1, num2):
    return num1 + num2

suma = sumar(15, 17)
print(suma)

def restar(num1 = 0, num2 = 2):
    return num1 - num2

resta = restar(4, 2)
print(resta)
resta = restar(num2= 6, num1 = 2)
print(resta)

resta = restar(8)
print(resta)

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "El segundo valor debe ser mayor que 0"

print(multiplicar(4, 2))
print(dividir(20, 5))
