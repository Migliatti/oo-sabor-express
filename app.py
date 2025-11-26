from models.restaurantes import Restaurante

restaurante = Restaurante('Pizza Hut', 'Pizza')
restaurante2 = Restaurante('Burger King', 'Hamburguer')
restaurante3 = Restaurante('Taco Bell', 'Mexicano')

restaurante.alternar_status()

def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()
    print('Aplicação encerrada com sucesso!')
