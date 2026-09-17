from abc import ABC, abstractclassmethod

class ItemCardapio(ABC):
    itens = []
    def __init__(self, nome, preco) :
        self._nome = nome
        self._preco = round(preco, 3)

    @abstractclassmethod
    def aplicar_desconto(self):
        pass
