num = int(input('Digite um número:'))
print('''Escolha uma das bases seguintes para a conversão:
[ 1 ] Converter para Binário
[ 2 ] Converter para Octal
[ 3 ] Converter para Hexadecimal''')
opção = int(input('Sua opção:'))
if opção == 1:
    print(f'{num} convertido para BINÁRIO É {bin(num)[2:]}')
elif opção == 2:
    print(f'{num} convertido para OCTAL É {oct(num)[2:]}')
elif opção == 3:
    print(f'{num} convertido para HEXADECIMAL É {hex(num)[2:]}')
else:
    print('''OPÇÃO INVÁLIDA!
    ESCOLHA APENAS 1,2 OU 3''')