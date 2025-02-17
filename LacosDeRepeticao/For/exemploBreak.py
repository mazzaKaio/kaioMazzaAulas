alunos = ["John Snow", "Jesse Pinkman", "Aria Stark", "Tyrion Lannister", "Voldemort"]
chamado = "Aria Stark"

for pessoa in alunos:
    if pessoa.__eq__(chamado):
        print("\n{} está presente!".format(chamado))
        break
    else:
        print("{}...".format(pessoa))