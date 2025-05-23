def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

def porcentaje(a, b):
    return (a * b) / 100

if __name__ == "__main__":
    print("Calculadora básica")
    print("Operaciones: sumar, restar, multiplicar, dividir, porcentaje")
    op = input("Ingrese la operación: ").strip().lower()
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))

    if op == "sumar":
        print("Resultado:", sumar(a, b))
    elif op == "restar":
        print("Resultado:", restar(a, b))
    elif op == "multiplicar":
        print("Resultado:", multiplicar(a, b))
    elif op == "dividir":
        print("Resultado:", dividir(a, b))
    elif op == "porcentaje":
        print("Resultado:", porcentaje(a, b))
    else:
        print("Operación no válida")