listaPecas = []

#Cadastro das peças
def cadastrarPecas(cp): #Cp = Código da peça
    print('Você selecionou a opção de cadastrar peças.')
    print('Código da peça:{}'.format(cp))
    nome = input('Digite o NOME da peça:')
    fabricante = input('Digite o NOME do fabricante da peça:')
    valor = float(input('Digite o VALOR(R$) da peça:'))
    dicionarioPeca = {'codigo'        : cp,   #Dicionario dos dados inseridos
                      'nome'      : nome,
                      'fabricante': fabricante,
                      'valor'     : valor}
    listaPecas.append(dicionarioPeca.copy()) #Copia os dados para a lista


#Consultar as peças
def consultarPeca():
    while True:
        try:
            print('Você selecionou a opção de consultar peças.')
            opConsultar = int(input('Escolha a opção desejada:'
                            '\n1-Consultar todas as Peças'
                            '\n2-Consultar Peças por código'
                            '\n3-Consultar Peças por fabricante'
                            '\n4-Retornar\n>'))
#Consultar todas as peças
            if opConsultar == 1:
                for peca in listaPecas:  #Selecionar cada dicionário da lista
                    for key, value in peca.items(): #Selecionar cada conjunto chave/valor do dicionário (ex.: nome : mouse)
                        print('{} : {}'.format(key,value))
#Consultar as peças por código
            elif opConsultar == 2:
                entrada = int(input('Digite o CÓDIGO da peça:'))
                for peca in listaPecas:
                    if(peca['codigo'] == entrada): 
                        for key, value in peca.items():
                            print('{} : {}'.format(key,value))
#Consultar as peças por fabricante
            elif opConsultar == 3:
                entrada = input('Digite o FABRICANTE da peça:')
                for peca in listaPecas:
                    if(peca['fabricante'] == entrada):
                        for key, value in peca.items():
                            print('{} : {}'.format(key,value))
#Retornar ao menu principal
            elif opConsultar == 4: 
                break
            else:
                print('Digite uma opção válida.')
                continue
        except ValueError:
            print('Opção inválida.')
#Remover as peças
def removerPeca():
    print('Você selecionou a opção de remover peças.')
    entrada = int(input('Digite o código da peça que deseja remover:'))
    for peca in listaPecas: 
        if(peca['codigo'] == entrada): #Remove a peça de acordo com o código digitado
            listaPecas.remove(peca)




#Programa Principal

print('Bem-vindo ao Controle de Estoque da Bicicletaria do Gustavo Menezes Bacelete de Almeida')
pecas = 0 # Contador para a quantidade de peças cadastradas
while True:
    try:
        opcao = int(input('Escolha a opção desejada:\n1-Cadastrar peças\n2-Consultar peças\n3-Remover peças\n4-Sair\n>'))
        if opcao == 1: #Opção de cadastrar peças
            pecas = pecas + 1
            cadastrarPecas(pecas)
        elif opcao == 2: #Opção de consultar peças
            consultarPeca()
        elif opcao == 3: #Opção de remover peças
            removerPeca()
        elif opcao == 4: #Opção de encerrar o programa
            print('Programa encerrado.')
            break
        else: #Mensagem de erro caso o usuario não digite uma opção existente 
            print('Digite uma opção válida.')
            continue
    except ValueError:
        print('Opção inválida.')