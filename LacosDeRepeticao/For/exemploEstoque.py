produtos = ["Coca cola", "pepsi", "guanara", "fanta", "sprite", "h2o", "skol", "brahma", "tubaina", "dolly guarana"]
estoque = [350, 250 , 876, 15, 150, 346, 74, 25, 1, 34]
nivelMinimo = 80

for i, qntd in enumerate(estoque):
    if qntd < nivelMinimo:
        print("Produto '{}' está com nível baixo: {}".format(produtos[i], qntd)) 