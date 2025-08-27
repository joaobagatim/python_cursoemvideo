# ========== Tipos primitivos ==========
# int() -> 7, -4, 0, 9875
# float() -> 4.5, 0.076, -15.223, 7.0
# bool() -> True, False
# str() -> "Olá", "7.5", ""

# ========== Operação print(): ==========
# print("A soma vale", soma)
# print(f"A soma vale {soma})
# print("A soma vale {}".format{soma})

# ========== Exemplo ==========
print("EXEMPLO")
n1 = input("Digite um valor para o primeiro número: ")
print(type(n1))

n2 = int(input("Digite um valor para o segundo número: "))
print(type(n2))

# ========== Questão 01 ==========
print("\nQuestão 01 - Crie um código em python que leia dois numeros e mostre a soma entre eles.")
num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))
soma = num1 + num2
print(f"A soma de {num1} + {num2} é: {soma}")

# ========== Questão 02 ==========
print("\nQuestão 02 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.")
entrada = input('Digite algo: ')

print('=' * 30)
print(f'O tipo primitivo desse valor é: {type(entrada)}')
print('=' * 30)

# Informações possíveis
print(f'Só tem espaços? {entrada.isspace()}')
print(f'É um número? {entrada.isnumeric()}')
print(f'É alfabético? {entrada.isalpha()}')
print(f'É alfanumérico? {entrada.isalnum()}')
print(f'Está em letras maiúsculas? {entrada.isupper()}')
print(f'Está em letras minúsculas? {entrada.islower()}')
print(f'Está capitalizada (Title Case)? {entrada.istitle()}')
print('=' * 30)