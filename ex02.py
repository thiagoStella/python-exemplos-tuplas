''' Crie um programa que cadastre os funcionários de uma empresa e seus dependentes. O funcionário deve ser 
cadastrado com matrícula, nome e dependentes. Os dependentes devem ser inseridos dinamicamente em uma tupla'''
funcionarios = []
while True:
    nome = input('Nome do funcionario: ')
    matricula = input('Matricula: ')
    dependentes = tuple()
    while True:
        dependente = input('Adicionar dependente (ZERO para sair): ')
        if dependente == '0':
            break
        dependentes += (dependente,)
    funcionario = (nome, matricula, dependentes)
    funcionarios.append(funcionario)

    if input('Deseja cadastrar um novo funcionário? (s/n)').lower() == 'n':
        break
print(funcionarios)