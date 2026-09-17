from avaliacao import Avaliacao
from cardapio.itemcardapio import ItemCardapio
class Restaurante:
    '''Representa um restaurante e suas características'''

    restaurantes = []

    def __init__(self, nome, categoria):
        '''
        Inicializa uma instância da classe Restaurante:
        
        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        '''
        
        self._nome = nome.title()
        self._categoria = categoria
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        '''Retorna a representação em string do restaurante.'''

        return f'Restaurante: {self._nome} | Categoria: {self._categoria}'

    @classmethod
    def listar_restaurantes(cls): 
        '''Exibe uma lista dos restaurantes anteriormente cadastrados, exibindo o nome, categoria, avaliação e o status atual.'''

        print(f'{'Restaurantes:'.ljust(25)} | {'Categoria:'.ljust(25)} | {'Avaliação:'.ljust(25)} | {'Status:'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        '''Faz a representação dos status False para Inativo e True para Ativo'''

        return 'Inativo' if self._ativo == False else 'Ativo'

    def alterar_estado(self):
        '''Altera o Status do restaurante escolhido'''

        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        '''
        Registra uma avaliação para um restaurante específico.
        
        Parâmetros:
        - cliente(str): O nome do cliente que fez a avaliação.
        - nota(float): A nota dada pelo cliente.
        '''

        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    def adicionar_cardapio(self, item): 
        if isinstance(item, ItemCardapio) :
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self._nome}\n')
        for i,item in enumerate(self._cardapio, start = 1):
            if hasattr(item, 'descricao'):    
                print(f'{i}. Nome: {item._nome.ljust(25)} | Preço: R${str(item._preco).ljust(25)} | Descrição: {item.descricao}')
            else:
                print(f'{i}. Nome: {item._nome.ljust(25)} | Preço: R${str(item._preco).ljust(25)} | Tamanho: {item.tamanho}')


    @property
    def media_avaliacoes(self):
        '''Calcula e retorna a média de todas as notas dadas por restaurante.'''
        
        if not self._avaliacao:
            return '--'
        else:
            soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
            quantidade_notas = len(self._avaliacao)
            media_notas = round(soma_notas / quantidade_notas, 1)
            return media_notas