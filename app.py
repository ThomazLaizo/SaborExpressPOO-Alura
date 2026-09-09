from restaurante import Restaurante

restaurante_1 = Restaurante('Hog Beef', 'Churrascaria')
restaurante_1.receber_avaliacao('Shoji', 2)

restaurante_2 = Restaurante('Japan in Box', 'Oriental')

restaurante_3 = Restaurante('Los Hermanos', 'Mexicana')
restaurante_3.alterar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()