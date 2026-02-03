s1 = float(input('Primeiro segmento:'))
s2 = float(input('Segundo segmento:'))
s3 = float(input('Terceiro segmento:'))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima podem formar um triângulo')
    if s1 == s2 == s3:
        print('O triângulo formado é equilátero')
    elif s1 != s2 != s3 != s1:
        print('O triângulo formado é escaleno')
    else:
        print('O triângulo formado é isósceles')
else:
    print('Os segmentos acima não podem formar um triângulo')

