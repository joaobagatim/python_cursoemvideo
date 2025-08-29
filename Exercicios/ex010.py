# Questão 10
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar

real = float(input("Quanto dinheiro você tem na carteira? R$"))
dolar = real / 5.40
print(f"Com R${real:.2f} você pode comprar U$D{dolar:.2f}.")