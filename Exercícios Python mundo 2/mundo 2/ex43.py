peso = float(input('PESO EM KG:'))
altura = float(input('ALTURA EM METROS:'))
IMC = peso / altura ** 2
print(f'Seu IMC é de {IMC:.1f}')
if IMC < 18.5:
    print(f'Com {peso} KG vocẽ está abaixo do peso ideal')
elif IMC >= 18.5 and IMC <= 25.0:
    print('PESO IDEAL')
elif IMC > 25 and IMC <= 30:
    print('Sobrepeso')
elif IMC >30 and IMC <= 40:
    print('''OBESIDADE!!!
    Faça um regime!''')
else:
    print('''Obesidade Mórbida
    Procure ajuda médica''')

