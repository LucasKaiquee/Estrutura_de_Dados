class Carro:
    def __init__(self, marca, cor, portas):
        self.marca = marca
        self.cor = cor
        self.portas = portas
    
    def acelerar(self):
        print("Estou acelerando")

    def frear(self):
        print("Estou freiando")

    def exibirModelo(self):
        print(self.marca, self.cor, self.portas)
    
carro1 = Carro("BMW", "Azul", "2 Portas")
carro2 = Carro("Audi", "Preto", "4 Portas")
carro3 = Carro("Mercedes", "Branca", "2 Portas")

carro1.exibirModelo()
carro2.acelerar()
carro3.frear()