#Questão 04
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

entrada = input("Digite algo: ")
print("=" * 15)
print(f"O tipo primitivo desse valor é: {type(entrada)}")
print("=" * 15)

print(f"Só tem espaços? {entrada.isspace()}")
print(f"É um número? {entrada.isnumeric()}")
print(f"É alfabético? {entrada.isalpha()}")
print(f"Está em letras maiúsculas? {entrada.isupper()}")
print(f"Está em letras minusculas? {entrada.islower()}")
print(f"Está capitalizada (Title Case)? {entrada.istitle()}")
print("=" * 15)