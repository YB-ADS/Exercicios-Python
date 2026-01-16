casa = float(input('Qual é o valor da casa em R$?'))
salario = float(input('Quanto é o seu salário em R$?'))
anos = float(input('Em quantos anos vocẽ pretende pagar o imóvel?'))
prestação = casa / (anos * 12)
mínimo = salario * 30 / 100
print(f'Para pagar um imóvel de R${casa}, em {anos} anos as prestações serão de R${prestação} ')
if prestação<=mínimo:
    print('EMPRÉSTIMO PODE SER CONCEDIDO!')
else:
    print('EMPRÉSTIMO NEGADO!!!')


