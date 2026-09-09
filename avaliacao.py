class Avaliacao:
    def __init__(self, cliente, nota):
        '''
        Inicializa uma instância da classe Avaliação
        
        Parâmetros:
        - cliente(str): O nome do cliente que fez a avaliação.
        - nota(float): A nota dada pelo cliente.
        '''
        
        self._cliente = cliente
        self._nota = nota 
        