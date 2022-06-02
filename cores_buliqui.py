import os
from time import sleep


def cor_pro_print_cor(cor):
    cores = {
        'vermelho': 31,
        'verde': 32,
        'amarelo': 33,
        'azul': 34,
        'rocho': 35,
        'azulClaro': 36,
        'cinza': 30,
        'branco': 37
    }
    return cores[cor]


def cor_pro_print_fundo(cor):
    cores = {
        'vermelho': 41,
        'verde': 42,
        'amarelo': 43,
        'azul': 44,
        'rocho': 45,
        'azulClaro': 46,
        'cinza': 40,
        'branco': 47
    }
    return cores[cor]


class Todas_cores:
    # cores
    cor_azul = '\033[1;34m'
    cor_vermelho = '\033[1;31m'
    cor_verde = '\033[1;32m'
    cor_amarelo = '\033[1;33m'
    cor_rocho = '\033[1;35m'
    cor_azul_claro = '\033[1;36m'
    cor_cinza = '\033[1;30m'
    cor_branco = '\033[1;37m'
    cor_limpar = '\033[m'


def linha(cor='branco', fundo='cinza', linha='===='):
    print('\033[1;{};{}m{}{}'.format(cor_pro_print_cor(cor),
                                     cor_pro_print_fundo(fundo),
                                     linha,
                                     '\033[m')*20)


def print_mod(text, cor='branco', fundo_cor='cinza'):
    cor_mod = cor_pro_print_cor(cor)
    fundo = cor_pro_print_fundo(fundo_cor)
    print(f'\033[1;{cor_mod};{fundo}m{text}\033[m')


def input_mod(text, cor='branco', fundo_cor='cinza'):
    cor_mod = cor_pro_print_cor(cor)
    fundo = cor_pro_print_fundo(fundo_cor)
    inpu = input(f'\033[1;{cor_mod};{fundo}m{text}\033[m')
    return inpu


def ferificador_input(op: str, quant_op: int):
    tentativas = 0
    error = False
    while error is False:
        if op.isnumeric():
            if int(op) > quant_op or int(op) < 1:
                tentativas += 1
                if tentativas > 5:
                    print_mod('Muitas tentativas!!', 'vermelho')
                    sleep(2)
                    os.system('cls')
                    return

                print_mod('Error opçao invalida!!', 'vermelho')
                op = input_mod('Qual e sua opçao: ', 'azulClaro')
                continue
            return int(op)
        else:
            tentativas += 1
            if tentativas > 5:
                print_mod('Muitas tentativas!!', 'vermelho')
                sleep(2)
                os.system('cls')
                return
            print_mod('Error opçao invalida!! isso nao e um numero!',
                      'vermelho')
            op = input_mod('Qual e sua opçao: ', 'azulClaro')
            if op.isnumeric():
                if int(op) > quant_op or int(op) < 1:
                    print_mod('Error opçao invalida!!', 'vermelho')
                    op = input_mod('Qual e sua opçao: ', 'azulClaro')
                    continue
                return int(op)
            else:
                continue


cores = Todas_cores()
