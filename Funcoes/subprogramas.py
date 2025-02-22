def getNome():
    nomeUsuario = input("Digite o seu nome: ")
    return nomeUsuario

def printMensagem(nomeUsuario):
    print("Olá Jovem Padawan", nomeUsuario)

def main():
    nomeUsuario = getNome()
    printMensagem(nomeUsuario)

main()
