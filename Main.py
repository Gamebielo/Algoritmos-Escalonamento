from funcoes import *

# MAIN


while True:
    # Chamando o Menu
    menu()

    typeAlg = int(input('Escolha o algorítmo: '))

    if typeAlg == 0:
        break

    # Caso o usuário entre com uma opção errada
    while typeAlg < 1 or typeAlg > 5:
        print('Opção Inválida, escolha os números de 1 até 5!')
        typeAlg = input('Escolha o algorítmo:\n')

    # FCFS
    if typeAlg == 1:
        fcfs()

    # SJF
    if typeAlg == 2:
        sjf()

    # Round Robin (RR)
    if typeAlg == 3:
        rr()
