# Questão 17
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))
hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)
print(f"A hipotenusa vai medir {hipotenusa:.2f}")

# ========= OU =========


print("\nOutra forma de ser feito:")
import math
cateto_oposto2 = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente2 = float(input("Digite o comprimento do cateto adjacente: "))
hipotenusa2 = math.hypot(cateto_oposto2, cateto_adjacente2)
print(f"A hipotenusa vai medir {hipotenusa2:.2f}")