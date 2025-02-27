import operacoes  
import utils 

operador = str(input('Digite o operador que deseja realizar: '))

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if operador == "+":
    resultado = operacoes.soma(num1, num2)
elif operador == "-":
    resultado = operacoes.sub(num1, num2)
elif operador == "/":
    resultado = operacoes.div(num1, num2)
elif operador == "*":
    resultado = operacoes.mult(num1, num2)
    

utils.exibir_resultado(operador, resultado)  



