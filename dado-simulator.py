import time, os, random 
#
print('Bem vindo ao gira-dado ')
#
time.sleep(2)
os.system('cls')
tamanho = int(input('Qual tamanho do dado você deseja girar? '))
dado = random.randint(1, tamanho)
girar = str(input('Deseja girar o dado? (s/n) ')).upper()
if girar == 'SIM' or girar == 'S':
    print('D{}'.format(dado))
elif girar == 'NAO' or girar == 'N':
    print('Ok! saindo.')
    #
