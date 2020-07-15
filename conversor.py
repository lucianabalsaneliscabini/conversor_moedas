import estrutura
from sys import exit
from time import sleep

while True:
    # Lista com todos os dados relacionados a moeda
    lista_convert = [('US$','DÓLAR AMERICANO', 5.35), ('C$','DÓLAR CANADENSE', 3.94), ('A$','DÓLAR AUSTRALIANO', 3.73), ('€','EURO', 6.08), ('¥','IENE', 0.050), ('£','LIBRA ESTERLINA', 6.74), ('Fr','FRANCO SUÍÇO', 1.91), ('$','PESO ARGENTINO', 0.075)]
    try:
        valor = estrutura.leiaValor('Quantidade de dinheiro que você possui: R$ ')
        print()
    except ValueError:
        print('\033[31mERRO, o sistema não aceita este tipo de caractere.\033[m')
        sleep(0.6)
        print('ENCERRANDO ...')
        sleep(1)
        exit()
    # Estruturação da tabela com os câmbios
    estrutura.linha('TABELA DE CÂMBIO')
    estrutura.tabela(0, lista_convert[0][0], lista_convert[0][1])
    estrutura.tabela(1, lista_convert[1][0], lista_convert[1][1])
    estrutura.tabela(2, lista_convert[2][0], lista_convert[2][1])
    estrutura.tabela(3, lista_convert[3][0], lista_convert[3][1])
    estrutura.tabela(4, lista_convert[4][0], lista_convert[4][1])
    estrutura.tabela(5, lista_convert[5][0], lista_convert[5][1])
    estrutura.tabela(6, lista_convert[6][0], lista_convert[6][1])
    estrutura.tabela(7, lista_convert[7][0], lista_convert[7][1])
    print()
    cambio = int(input('Qual câmbio você deseja comprar? '))
    # Impedindo que o usuário digite números inválidos
    while cambio not in range(0, 8):
        print('\033[31mERRO! ESCOLHA UMA OPÇÃO VÁLIDA\033[m')
        cambio = int(input('Qual câmbio você deseja comprar? '))
    print()
    # Confirmando o câmbio escolhido pelo usuário
    print('-=' * 20)
    print(f'CÂMBIO ESCOLHIDO: {lista_convert[cambio][1]}')
    print(f'VALOR: R$ {lista_convert[cambio][2]}')
    print('-=' * 20)
    # Conversão para a moeda escolida
    tot = valor / lista_convert[cambio][2]
    print(f'TOTAL: {lista_convert[cambio][0]} {tot:.2f}')
    print('-=' * 20)
    print()
    # Continuar o laço ou não
    continuar = input('Deseja realizar outra operação? [S/N] ').upper()
    while continuar == 'S':  
        print()
        print('-=' * 20)
        break
    else:
        print('\033[34mOBRIGADA ! VOLTE SEMPRE\033[m')
        break

