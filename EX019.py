import random
alu1 = str(input('Primeiro aluno: '))
alu2 = str(input('Segundo aluno: '))
alu3 = str(input('Terceiro aluno: '))
alu4 = str(input('Quarto aluno: '))
lista = [alu1, alu2, alu3, alu4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))




