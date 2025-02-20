vendasTecnologia = {"iphone":"15000", "samsung galaxy":"12000", "tv samsung":"10000", "ps4":"14300", "tablet":"1720", "ipad":"1200"}

for chave in vendasTecnologia:
    print(chave)

print("\nOutra pratica do for\n")
for chave in vendasTecnologia:
    print("O produto {} vendeu {} unidades!".format(chave, vendasTecnologia[chave]))