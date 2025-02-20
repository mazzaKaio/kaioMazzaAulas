vendasTecnologia = {"iphone":"15000", "samsung galaxy":"12000", "tv samsung":"10000", "ps4":"14300", "tablet":"1720", "ipad":"1200"}

for produto, vendas in vendasTecnologia.items():
    print("{} vendeu {} unidades!".format(produto, vendas))