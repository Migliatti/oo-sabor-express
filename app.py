from models.restaurantes import Restaurante
import random

restaurante = Restaurante('Pizza Hut', 'Pizza')
restaurante2 = Restaurante('Burger King', 'Hamburguer')
restaurante3 = Restaurante('Taco Bell', 'Mexicano')
restaurante.receber_avaliacao('João', random.randint(1, 10))
restaurante.receber_avaliacao('Maria', random.randint(1, 10))
restaurante.receber_avaliacao('Pedro', random.randint(1, 10))
restaurante.receber_avaliacao('Ana', random.randint(1, 10))
restaurante.receber_avaliacao('Bruno', random.randint(1, 10))
restaurante.alternar_status()
restaurante2.receber_avaliacao('João', random.randint(1, 10))
restaurante2.receber_avaliacao('Maria', random.randint(1, 10))
restaurante2.receber_avaliacao('Pedro', random.randint(1, 10))
restaurante2.receber_avaliacao('Ana', random.randint(1, 10))
restaurante2.receber_avaliacao('Bruno', random.randint(1, 10))
restaurante2.alternar_status()
restaurante3.receber_avaliacao('João', random.randint(1, 10))
restaurante3.receber_avaliacao('Maria', random.randint(1, 10))
restaurante3.receber_avaliacao('Pedro', random.randint(1, 10))
restaurante3.receber_avaliacao('Ana', random.randint(1, 10))
restaurante3.receber_avaliacao('Bruno', random.randint(1, 10))
restaurante3.alternar_status()


def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()
    print('Aplicação encerrada com sucesso!')
