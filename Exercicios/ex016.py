# Questão 16
# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira

import math

num_real = float(input("Digite um número real: "))
print(f"O número {num_real} tem a parte inteira igual a {math.trunc(num_real)}")