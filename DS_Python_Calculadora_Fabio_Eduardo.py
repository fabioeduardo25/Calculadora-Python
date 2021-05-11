operacao = input('''
Digite a operação matemática que você vai fazer:
+ Adição
- Subtração
/ Divisão
* Multiplicação
** Expoente
''')

num_1 = int(input('Digite seu primeiro numero: '))
num_2 = int(input('Digite seu segundo numero: '))

if operacao == '+':
    print('{} + {} = '.format(num_1, num_2))
    print(num_1 + num_2)

elif operacao == '-':
    print('{} - {} = '.format(num_1, num_2))
    print(num_1 - num_2)

elif operacao == '/':
    print('{} / {} = '.format(num_1, num_2))
    print(num_1 / num_2)

elif operacao == '*':
    print('{} * {} = '.format(num_1, num_2))
    print(num_1 * num_2)

elif operacao == '**':
    print('{} ** {} = '.format(num_1, num_2))
    print(num_1 ** num_2)

else:
    print('Operação Invalida, por favor faça novamente.')
