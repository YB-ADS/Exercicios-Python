# Programa que lê duas notas e mostra se o alunos está de recuperação, reprovado ou aprovado
n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
media = (n1 + n2)/2
if 5 <= media < 7:
    print(f' O aluno está reprovado com média {media:.1f}')
elif media < 5:
    print(f'Aluno reprovado com média {media:.1f}')
elif media >= 7.0:
    print(f'APROVADO COM MÉDIA {media:.1f}')
