from datetime import date
print('----CONFEDERAÇÃO NACIONAL DE NATAÇÃO----')
nascimento = int(input('Qual é o seu ano de nascimento?'))
anoatual = date.today().year
idade = anoatual - nascimento
print(f'O atleta tem {idade} anos')
if idade <= 9:
    print('COMPETIDOR MIRIM')
elif idade <= 14:
    print('COMPEIDOR INFANTIL')
elif idade <=19:
    print('COMPETIDOR JÚNIOR')
elif idade <=25:
    print('COMPETIDOR SÊNIOR')
else:
    print('COMPETIDOR MASTER')