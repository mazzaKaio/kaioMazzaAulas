# Faça um programa que receba uma nota do aluno e se for SUPERIOR ou IGUAL a 7 apareça mensagem que ele está APROVADO
# se for INFERIOR a 5 ele está "Não aprovado/reprovado direto" e se estiver entre 5 e 7 apareça a mensagem "não aprovado/recuperação"

notaAluno = float(input("Digite a nota do aluno:"))

if notaAluno >= 7:
    print("O aluno foi APROVADO!")
elif notaAluno < 5:
    print("O aluno foi REPROVADO!")
else:
    print("O aluno está de RECUPERAÇÃO!")