from datetime import date
from time import sleep
print('Verificando a categoria de atletas...')
ano = date.today().year
while True:
    nascimento = int(input('Digite o ano de nascimento: '))
    idade = ano - nascimento
    print('\033[1m>>>> Verificando <<<<\033[m')
    sleep(1)
    print('-'*35)
    print(f'O atleta tem {ano - nascimento} anos.')
    if idade <= 9:
        print('Está na categoria \033[1MMIRIM!\033[m')
    elif idade <= 14:
        print('Está na categoria \33[1mINFANTIL!\033[m')
    elif idade <= 19:
        print('Está na categoria \033[1mJUNIOR!\033[m')
    elif idade <= 25:
        print('Está na categoria \033[1mSÊNIOR!\033[m')
    else:
        print('Está na categoria \033[1mMASTER!\033[m')
    while True:
        print('-' * 40)
        resp = str(input('Quer continuar? (S/N) ')).strip().upper()[0]
        if resp in 'SN':
            break
        else:
            print('Por favor digite apenas S ou N.')
    if resp in 'N':
        print('\033[1mFinalizando...\033[m')
        sleep(1)
        break
print('='*40)
print('Programa Finalizado')
