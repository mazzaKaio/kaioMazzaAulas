# Faça um programa que o usuário digite um número e diga se o número é superior a 20, inferior a 10 ou se está entre 10 e 20
num = int(input("Digite um número inteiro:"))

if num > 20:
    print(num, "é maior que 20")
elif num < 10:
    print(num, "é menor que 10")
else:
    print(num, "está entre 10 e 20")