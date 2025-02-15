produtos = ["apple", "tv", "mac", "iPad"]
novosProdutos = ["iPhone"]

print("Usando 'extend':")
produtos.extend(novosProdutos)
print(produtos)

print("\nUsando '+':")
novosProdutos = ["celular"]
produtos += novosProdutos
print(produtos)

print("\nUsando 'append':")
novosProdutos = ["macbook"]
produtos.append(novosProdutos)
print(produtos)