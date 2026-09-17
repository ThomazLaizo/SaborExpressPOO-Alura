from restaurante import Restaurante
from cardapio.porcao import Porcao
from cardapio.bebida import Bebida
from cardapio.prato import Prato

restaurante_1 = Restaurante('Hog Beef', 'Churrascaria')

restaurante_2 = Restaurante('Japan in Box', 'Oriental')

restaurante_3 = Restaurante('Dona Benta', 'Padaria')

bebida_suco = Bebida('Suco de Melancia', 5.00, 'Grande')
bebida_suco.aplicar_desconto()

prato_pao = Prato('Pão Francês', 1.50, 'O melhor da cidade!')
prato_pao.aplicar_desconto()

porcao_sushi = Porcao('Porção_Sushi', 10.00, 'Médio')
porcao_sushi.aplicar_desconto()

restaurante_3.adicionar_cardapio(prato_pao)
restaurante_3.adicionar_cardapio(bebida_suco)
restaurante_2.adicionar_cardapio(porcao_sushi)

def main():
    restaurante_2.exibir_cardapio


if __name__ == '__main__':
    main()