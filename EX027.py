nome = str(input('Digite seu nome completo: ')).strip()
print('Muito prazer em te conhecer  {}'.format(nome))
n1 = nome.split()
print('Seu primeiro nome é {}'.format(n1[0]))
print('Seu ultimo nome é {}'.format(n1[len(n1)-1]))

