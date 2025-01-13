nome = 'Carlos Vinicius'

print(nome[7:12])

print(nome[7:12:2]); """ pula de 2 em dois """

print(len(nome[7:12]))

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}') 
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')

