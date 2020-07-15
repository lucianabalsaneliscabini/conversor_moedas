# Organização da estrutura principal da tabela
def tabela(pos, simbolo, nome):
    print(f'[ {pos} ]', end=' ')
    print(f'\t{simbolo}', '-' * (10 - len(simbolo)), end=' ')
    print(f'{nome}')

# Estilização do título
def linha(palavra):
    print('~' * 40)
    print(palavra.center(40))
    print('~' * 40)

#  Verficiação do preço digitado pelo usuário
def leiaValor(cont):
    valor = input(cont).strip()
    while valor.isalpha() or valor == '':
        print(f'\033[31mERRO, "{valor}" não é um preço inválido!\033[m')
        valor = input(cont) 
    return float(valor.replace(',', '.'))
