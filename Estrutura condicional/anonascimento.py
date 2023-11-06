# faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
an = int(input())
idade = 2023 - an
print(f'Voce tem {idade} anos')
# se ela ainda vai se alistar ao serviço militar.
if idade < 18:
    print('Voce ainda vai se alistar')
    tp = 18 - idade
    print(f'Ainda falta {tp} anos')
# se é a hora de se alistar.
elif idade == 18:
    print('Já esta na hora de se alistar')
# se já passou do tempo de alistamento.
elif idade > 18:
    print('já passou a hora ')
    tp = idade - 18
    print('Você deveria ter se alistado a {tp} anos')
# Seu programa tambem deverá mostrar o tempo que falta ou que ja passou do prazo



