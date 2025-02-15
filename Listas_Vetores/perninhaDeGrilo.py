nomesClientes = ["Kaio", "Daniel", "Sergio", "Eberth", "Caio"]
telefonesClientes = ["47985", "47555", "47326", "47121", "473658"]
bairrosCleintes = ["Comasa", "Boa Vista", "Iririu", "Centro", "Norte"]

nomeRequisitado = input("Digite o nome do cliente: ").title()

if nomeRequisitado in nomesClientes:
    i = nomesClientes.index(nomeRequisitado)
    fone = telefonesClientes[i]
    bairro = bairrosCleintes[i]
    print("\nCliente encontrado!\nNome do cliente: {}\nTelefone do cliente: {}\nBairro do cliente: {}".format(nomeRequisitado, fone, bairro))
else:
    print("\nCliente '{}' não encontrado ou não cadastrado!".format(nomeRequisitado))