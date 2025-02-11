notaAluno = float(input("Digite a nota do aluno:"))

if notaAluno >= 7:
    print("O aluno foi APROVADO!")
else:
    if notaAluno >= 5:
        print("O aluno está de RECUPERAÇÃO!")
    else:
    print("O aluno foi REPROVADO!")