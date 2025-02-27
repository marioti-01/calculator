def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    while b == 0:
        b = int(input("Digite um numero válido: "))
    return a / b
