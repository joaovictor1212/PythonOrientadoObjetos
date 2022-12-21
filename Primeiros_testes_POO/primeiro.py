#Primeira atribuição com Orientação a Objetos



class Carros:

    def __init__(self, marca, nome, potencia, ano):
        self.marca = marca
        self.nome = nome
        self.potencia = potencia
        self.ano = ano

    def Preco_Do_Carro(self, preco):
        print("O preco do carro é: ", preco)


    def Cor_Do_Carro(self, cor):
        print('O carro é da cor: ', cor)


    def Informacoes_Do_Carro(self):
        print(self.marca, self.nome, self.potencia, self.ano)


carro = Carros('Chevrolet', 'Celta', '68CV', 2010)

carro.Informacoes_Do_Carro()

carro.Cor_Do_Carro('Prata')

carro.Preco_Do_Carro('R$20000,00')

