from temporizador import Temporizador

class SemafaroTemporizado:
    def __init__(self): 
        # 1: verde, 2: amarelo, 3: vermelho
        self.estadoAtual = 1
        self.timer = Temporizador()
        self.tempoTransicao = {1:20, 2:5, 3:10}

    def getEstadoAtual(self)->str:
        if self.estadoAtual == 1:
            return 'Verde'
        elif self.estadoAtual ==2:
            return 'Amarelo'
        else:
            return 'Vermelho'