from time import sleep
from cores_buliqui import print_mod, linha, input_mod, ferificador_input
from random import randint
import os
os.system('cls')

nome_person = ''

linha('azulClaro')
print_mod('{:^80}'.format('jogo rpg terminal'), 'azulClaro')
linha('azulClaro')
print_mod('ESCOLA SUA CLASSE', 'azulClaro')
linha('azulClaro')


def criar_menu_personagens():
    linha('azulClaro')
    print_mod('[1]- mago', 'azulClaro')
    print_mod('[2]- arqueiro', 'azulClaro')
    print_mod('[3]- atirador', 'azulClaro')
    linha('azulClaro')


criar_menu_personagens()
op = input_mod('qual e sua classe: ', 'azulClaro')
op = ferificador_input(op, 3)

op_maquina = []
op_jogador = []


def menu_poder(poder):
    linha('azulClaro')
    print_mod(f'[1]- {poder[0]}', 'azulClaro')
    print_mod(f'[2]- {poder[1]}', 'azulClaro')
    print_mod(f'[3]- {poder[2]}', 'azulClaro')
    linha('azulClaro')

    op = input_mod('Qual e seu Poder: ', 'azulClaro')
    op = ferificador_input(op, 3)

    return int(op)


# maquina
op_maquina_m = randint(1, 3)
nome_perso_maquina = ''

if op_maquina_m == 1:
    nome_perso_maquina = 'mago'
    op_maquina = ['bola de fogo', 'raio', 'cura']
elif op_maquina_m == 2:
    nome_perso_maquina = 'arqueiro'
    op_maquina = ['flechha de fogo', '200 flechas pro alto', 'cura']
elif op_maquina_m == 3:
    nome_perso_maquina = 'atirador'
    op_maquina = ['tiro', 'metralha', 'cura']

# batalhar


def ferificar_se_acabo(vida_jogador, vida_maquina):
    if vida_maquina == 0 or vida_maquina < 0:
        print_mod(
            f'acabou voçe ganhou com {vida_jogador} de vida', 'verde')
        sleep(3)
        os.system('cls')
        perdeu = True
        return perdeu
    if vida_jogador == 0 or vida_jogador < 0:
        print_mod(
            f'acabou voçe perdeu a maquina ganhou com {vida_maquina} de '
            'vida', 'vermelho')
        sleep(3)
        os.system('cls')
        perdeu = True
        return perdeu
    perdeu = False
    return perdeu


def batalhar(op_jogador, person):
    vida_maquina = 80
    vida_jogador = 80

    linha('azulClaro')
    print_mod(
        f'A maquina Escoleu o {nome_perso_maquina} E voçes escoleu {person} '
        'e voçes vão batalhar!!',
        'azulClaro')
    print_mod('1.', 'azulClaro')
    sleep(2)
    print_mod('2..', 'azulClaro')
    sleep(2)
    print_mod('3...', 'azulClaro')
    sleep(2)
    print_mod('BATALHAR!!', 'azulClaro')
    linha('azulClaro')
    print_mod(
        f'Qual poder voçe vai jogar nele ele esta com {vida_maquina} vida ',
        'azulClaro')
    linha('azulClaro')
    perdeu = False
    while not perdeu:
        messagens = ''
        op = menu_poder(op_jogador)
        if op == 1:
            if person == 'mago':
                vida_maquina -= 20
                messagens = 'bola lancada.. Voce tirou 20 de dano'

            if person == 'arqueiro':
                vida_maquina -= 20
                messagens = 'fecha de fogo lancada.. Voce tirou 20 de dano'

            if person == 'atirador':
                vida_maquina -= 20
                messagens = 'deu o tiro.. Voce tirou 20 de dano'

        if op == 2:
            if person == 'mago':
                vida_maquina -= 10
                messagens = 'raio lancado... Voce tirou 10 de dano do'
            if person == 'arqueiro':
                vida_maquina -= 10
                messagens = '200 flechas pro alto lancada.. Voce tirou 10 de'
                'dano'

            if person == 'atirador':
                vida_maquina -= 10
                messagens = 'metralha.. Voce tirou 10 de dano'

        if op == 3:
            if vida_jogador == 80 or vida_jogador > 75:
                messagens = 'Vida esta cheia'
            else:
                vida_jogador += 5
                messagens = 'curar.. Voce curou 5 de vida agora voçe esta com'
                f'{vida_jogador}'

        op_maquina_m = randint(1, 3)

        messagens_maquina = ''
        if op_maquina_m == 1:
            if nome_perso_maquina == 'mago':
                vida_jogador -= 20
                messagens_maquina = 'maquina jogou bola de fogo.. Voce perdeu'
                '20 de'
                'vida'

            if nome_perso_maquina == 'arqueiro':
                vida_jogador -= 20
                messagens_maquina = 'maquina jogou flecha de fogo.. Voce'
                'perdeu 20 de'
                'vida'

            if nome_perso_maquina == 'atirador':
                vida_jogador -= 20
                messagens_maquina = 'maquina te deu um tiro.. Voce perdeu 20'
                'de vida'

        if op_maquina_m == 2:

            if nome_perso_maquina == 'mago':
                vida_jogador -= 10
                messagens_maquina = 'maquina jogou raio.. Voce prdeu 10 de'
                'vida'

            if nome_perso_maquina == 'arqueiro':
                vida_jogador -= 10
                messagens_maquina = 'maquina jogou 200 flechas pro alto.. Voce'
                'perdeu'
                '10 de'

            if nome_perso_maquina == 'atirador':
                vida_jogador -= 10
                messagens_maquina = 'maquina metralou voçe.. Voce perdeu 10 de'
                'vida'

        if op_maquina_m == 3:
            vida_maquina += 5
            messagens_maquina = 'maquina usou cura.. curou 5 de vida'

        perdeu = ferificar_se_acabo(vida_jogador, vida_maquina)

        linha('azulClaro')
        print_mod(messagens, 'azulClaro')

        print_mod('maquina esta jogando........', 'vermelho')
        sleep(2)
        linha('vermelho')
        print_mod(messagens_maquina, 'vermelho')
        linha('vermelho')
        linha('azulClaro', linha='=-=')
        print_mod(f'SUA VIDA => \033[31m{vida_jogador}\033[m', 'azulClaro')
        print_mod(
            f'VIDA DO INIMIGO => \033[31m{vida_maquina}\033[m', 'azulClaro')
        linha('azulClaro', linha='=-=')


# jogador
if op == 1:
    nome_person = 'mago'
    op_jogador = ['bola de fogo', 'raio', 'cura']
    batalhar(op_jogador, nome_person)


if op == 2:
    nome_person = 'arqueiro'
    op_jogador = ['flechha de fogo', '200 flechas pro alto', 'cura']
    batalhar(op_jogador, nome_person)

if op == 3:
    nome_person = 'atirador'
    op_jogador = ['tiro', 'metralha', 'cura']
    batalhar(op_jogador, nome_person)
