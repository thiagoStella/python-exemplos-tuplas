''' Crie um programa que efetue o cadastro de produtos e preços. Caso o produto já exista, deve perguntar se o usuário pretende atualizar o valor.
Imprima o dicionário no fim do programa em formato de lista.'''
estoque = {}

while True:
    produto = input('Digite o nome do produto: ')
    if produto in estoque:
        if input(f'Produto já cadastrodo no sistema. Deseja atualizar? (s/n)') =='n':
            break    
    preco = float(input('Digite o preço: '))
    estoque[produto] = preco
    if input('Deseja cadastrar mais produtos? (s/n)') =='n':
        break
for item in estoque:
    print(f'{item:>20}: R${estoque[item]:.2f}')
