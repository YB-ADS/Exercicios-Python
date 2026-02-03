preco = float(input('Preço das compras em R$:'))
print('''Qual é a forma de pagamento?
[ 1 ] Á vista/Cheque tem 10% de Desconto!
[ 2 ] Á vista no cartão recebe 5% de Desconto
[ 3 ] Em até 2x no cartão: preço formal
[ 4 ] 3x ou mais no cartão tem 20% de juros''')
opcão = int(input('Escolha uma das opções:'))
if opcão == 1:
    resultado = preco - (preco * 10/100)
    print(f'Valor com DESCONTO R${resultado:.2f}')
elif opcão == 2:
    resultado = preco - (preco * 5/100)
    print(f'Valor com Desconto R${resultado:.2f}')
elif opcão == 3:
    resultado = preco/2
    print(f'''Em até 2x vezes no cartão o preço é formal R${preco:.2f} 
e dividido no cartão em 2x fica duas parcelas de R${resultado}''')
elif opcão == 4:
    resultado = preco + (preco * 20/100)
    print(f'Com juros o Valor é de R${resultado:.2f}')



