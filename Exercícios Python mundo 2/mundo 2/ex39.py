# Alistamento Militar
from datetime import date
print("--------ALISTAMENTO MILITAR--------")
anodenascimento = int(input('Digite seu ano de nascimento:'))
anoatual = date.today().year
idade = anoatual - anodenascimento
print(f'Quem nasceu em {anodenascimento} tem {idade} em {anoatual}')
if idade ==18:
    print('VOCÊ DEVE SE ALISTAR JÁ')
elif idade <18:
    saldo = 18 - idade
    ano = anoatual + saldo
    print(f'Vocẽ tem {idade} anos e deve se alistar daqui {saldo} em {ano}')
elif idade > 18:
    saldo = idade - 18
    ano = anoatual - saldo
    print(f'''VOCẼ ESTÁ EM DÉBITO COM O EXÉRCITO
    DEVERIA TER SE ALISTADO EM {ano} A {saldo} ANOS ATRÁS''')
