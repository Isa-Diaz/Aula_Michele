estoque = {"blusa":[300, 20.00], "calça":[300, 30.00], "moletom":[300, 50.00], "tenis":[300, 40.00]}
vendido = [["blusa", 20], ["calça", 30], ["moletom", 50], ["tenis", 30]]
total = 0

for roupas in vendido:
    produto, quantidade = roupas
    preco = estoque[produto][1]
    lucro = preco * quantidade

print(f"{produto}: {quantidade} x {preco} = {lucro}")
estoque[produto][0] -= quantidade
total += lucro

for chave, dados in estoque.items():
    print("Produto:", chave)
    print("Quantidade:", dados[0])
    print(f"Preço: R${dados[1]}")
