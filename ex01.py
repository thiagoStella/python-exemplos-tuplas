'''Crie um programa que efetue o cadastro de pessoas com nome, RG e CPF por meio de tuplas, adicionando-as a uma lista e imprimindo essa lista no fim do programa.'''
cadastro = []
while True:
    nome = input('Digite o nome: ')
    rg = input('Digite o RG: ')
    cpf = input('Digite o CPF: ')
    pessoa = (nome, rg, cpf)
    cadastro.append(pessoa)
    if input('Deseja continuar cadastrando? (s/n)').lower() == 'n':
        break
print(cadastro)