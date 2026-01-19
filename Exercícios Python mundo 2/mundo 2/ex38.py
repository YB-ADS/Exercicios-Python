n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
if n1 > n2:
    print('O primeiro valor é MAIOR')
elif n2 > n1:
    print('O segundo valor é MAIOR')
elif n1 == n2:
    print('Não existe valor maior, os dois são IGUAIS')