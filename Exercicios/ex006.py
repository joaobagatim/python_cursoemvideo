# Questão 06
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

num = int(input("Digite um número: "))
dobro = num * 2
triplo = num * 3
raizQuadrada = num ** (1/2)
print(f"O dobro do número {num} vale {dobro}.\nO triplo de {num} vale {triplo}.\nA raiz quadrada de {num} vale {raizQuadrada:.2f}.")