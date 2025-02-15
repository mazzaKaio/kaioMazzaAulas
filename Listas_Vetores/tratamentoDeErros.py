produtos = ['tv', 'celular', 'mouse', 'teclado', 'tablet', 'geladeira', 'forno']
itemUsuario = input("Digite o item que você deseja remover: ").lower()

try:
    produtos.remove(itemUsuario)
    print(produtos)
except:
    print("O produto {} não existe na lista.".format(itemUsuario))