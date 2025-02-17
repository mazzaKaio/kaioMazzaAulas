vendas = [100, 50, 80, 190, 200, 210, 45, 37, 99, 105, 130, 111, 44, 24, 67, 93, 157, 25]
meta = 100
bateramMeta = 0

for venda in vendas:
    if venda >= meta:
        print(venda)
        bateramMeta += 1

numFuncionarios = len(vendas)
print("O percentual de funcionários que bateram a meta foi de {:.1}".format(bateramMeta/numFuncionarios))