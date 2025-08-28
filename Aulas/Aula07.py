# ========== Operações Aritméticas ==========
# '+' -> Adição
# '-' -> Subtração
# '*' -> Multiplicação
# '/' -> Divisão
# '**' -> Potência ou 'pow()'
# '//' -> Divisão Inteira
# '%' -> Resto da Divisão
# '==' -> Igual
# ========== Ordem de Precedência ==========
# 1- ()
# 2- **
# 3- *; /; //; %
# 4- +; -

# EXEMPLO 01
print("Exemplo 01")
nome = str(input("Qual é seu nome? "))
print(f"Prazer em te conhecer {nome:=^20}!")
print("\n")
print("="*15)
print("\n")

# EXEMPLO 02
print("Exemplo 02")
n1 = int(input("Um valor: "))
n2 = int(input("Outro numero: "))
soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
divInteira = n1 // n2
potencia = n1 ** n2
resto = n1 % n2
print(f"\nA soma é {soma}.\nA subtração é {subtracao}.\nA multiplicação é {multiplicacao}.\nA divisão {divisao:.2f}.\nA divisão inteira é {divInteira}.\nA potencia é {potencia}.\nO resto é {resto}.")