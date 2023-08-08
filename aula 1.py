#
# #Lista
#
# lista = ["alface", "batata", "tomate", "feijão"]
# print(lista)
#
# #Dicionario usa dois "componentes" alem de {} e :
# tabela = {"alface": 0.45, "batata":1.2, "tomate":2.3, "feijão":1.5}
# print(tabela)

#aula dicionario

carros = {"Jeep Renegade":['R$90.000,00', 'ano = 2020'],
          "Jeep Compass":['R$150.000,00', 'ano = 2020'],
          "Troller": ['R$200.000,00', 'ano = 2020']}
print(carros)
print(carros['Jeep Renegade'])

#altera o elemento unico da lista
#carros["Jeep Compass"] = 'R$180.000,00'

#como possui mais de um elemento devemos definir sua posição:
carros["Jeep Compass"][0] = 'R$180.000,00'
print(carros)
#altera um elemento de varios da lista
carros["Jeep Renegade"][1] = "ano =2020"
print(carros)

#O elemento Troller foi vendido, apague da lista:
del carros["Troller"]
print(carros)

#Adicionar novo elemento:

carros["audi"] = ['R$250.000,00', "2023"]
print(carros)

#Pesquisar se possui ou não um elemento na tabela
print("Audi" in carros)
print("BMW" in carros)

#Imprimir apenas chaves
print(carros.keys())

#Imprimir apenas valores
print(carros.values())
