# Juntando listas
Lista1 = [1,2,3,4,5]
Lista2 = [6,7,8,9,10]
Lista3 = [11,12,13,14,15]
todasListas = [Lista1, Lista2, Lista3]
print(todasListas)

# Aceesando o produto de um vetor pelo seu 'indéx'
print("-----------------------")
produtos = ['tv', 'celular', 'mouse', 'teclado', 'tablet']
print(produtos[1])

# Listas diferentes
print("-----------------------")
vendas = [1000, 1500, 350, 270, 900]
print("As vendas de {} foram R${}".format(produtos[0], vendas[0]))

# Metodo "INDEX"
print("-----------------------")
i =  produtos.index('mouse')
print("O valor de 'i' é: " + str(i))
print("O produto da posição 'i' é: " + str(produtos[i]))

# Continuação INDEX
produtos = ['tv', 'celular', 'mouse', 'teclado', 'tablet', 'geladeira', 'forno']
estoque = [100,150,100,120,70,180,80]

print("-----------------------")
produto = input("Insira o nome do produto: ").lower()
if produto in produtos:
    i = produtos.index(produto)
    qntdEstoque = estoque[i]
    print("\nTemos '{}' unidades de '{}' no estoque".format(qntdEstoque, produto))
else:
    print("\n'{}' não existe no estoque".format(produto))