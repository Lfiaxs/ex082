lista = []
pares = []
ímpares = []
while True:
    c = (int(input('Digite um número: ')))
    lista.append(c)
    if c % 2 == 0:
        pares.append(c)
    else:
        ímpares.append(c)
    escolha = str(input('Quer continuar? [S/N] '))
    if escolha in 'Nn':
        break
print('-='*30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {ímpares}')
