

print(12, 34, sep="*")
print("12-34")

nome = input('Qual o seu nome? ')
valor = 1563.9878877

if nome == 'carlos':
    print(f'O seu nome é {nome}')
    print('%s, o valor a ser pago é %.2f' % (nome, valor))
else:
    print('Seu nome não é carlos!')