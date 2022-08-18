#-----Começo da função dimensoesObjeto----
def dimensoesObjeto():
    while True: #Repetição infinita a não ser que tudo seja preenchido corretamente
        try: 
            altura = int(input('Digite a altura do objeto (em cm):')) #Pergunta a altura
            comprimento = int(input('Digite o comprimento do objeto (em cm):')) #Pergunta o comprimento
            largura = int(input('Digite a largura do objeto (em cm):')) #Pergunta a largura
            volume = altura * comprimento * largura  #Calcula o volume do objeto
            print('O volume do objeto(em cm³) é: {}'.format(volume)) #Mostra o volume do objeto pro usuário
        except ValueError: #Erro caso seja digitado algo além de números inteiros
            print('**Você digitou um valor não numérico.')
            print('**Insira novamente as dimensões. ')
            continue #Volta pro inicio da repetição
        
        if volume < 1000: #Se o volume for menor que 1000
            return 10 #Valor vai ser 10
        elif 1000 <= volume < 10000: #Se o volume for maior ou igual a 1000 e menor que 10000
            return 20 #Valor vai ser 20
        elif 10000 <= volume < 30000: #Se o volume for maior ou igual a 10000 e menor que 30000
             return 30 #Valor vai ser 30
        elif 30000 <= volume < 100000: #Se o volume for maior ou igual a 30000 e menor que 100000
             return 50 #Valor vai ser 50
        else: #Se o volume for maior que 100000 vai dar erro e irá repetir a pergunta
             print('**Nossa companhia não trabalha com volumes tão grandes.')
             print('**Entre com as dimensões desejadas novamente.')
             continue  #Volta pro inicio da repetição
#-----Fim da função dimensoesObjeto-------

#-----Começo da função pesoObjeto----
def pesoObjeto():
    while True: #Repetição infinita a não ser que seja preenchido corretamente
        try:
            peso = int(input('Digite o peso do objeto (em kg):')) #Pergunta o peso
        except ValueError: #Erro caso seja digitado algo além de números inteiros
            print('**Voce digitou um valor não numérico.')
            print('**Insira novamente um valor.')
            continue #Volta pro inicio da repetição
        if peso <= 0.1: #Se o peso for menor ou igual a 0.1 kg
            return 1
        elif 0.1 < peso <= 1: #Se o peso for maior que 0.1 kg e menor ou igual a 1 kg
            return 1.5
        elif 1 < peso <= 10: #Se o peso for maior que 1 kg e menor ou igual a 10 kg
            return 2
        elif 10 < peso <= 30: #Se o peso for maior que 10 kg e menor ou igual a 30
            return 3
        else: #Se o peso for maior que 30 retornará para a pergunta
            print('**Nossa companhia não trabalha com objetos tão pesados.')
            print('**Insira um peso aceitável pela companhia.')
            continue # Retorna pro inicio da repetição
#-----Fim da função pesoObjeto-------

#-----Começo da função rotaObjeto---- 
def rotaObejto():
    while True: #Repetição infinita a não ser que seja preenchido corretamente
        print('Selecione a rota desejada:')
        print('RS - De Rio de Janeiro até São Paulo') 
        print('SR - De São Paulo até Rio de Janeiro') 
        print('BS - De Brasília até São Paulo') 
        print('SB - De São Paulo até Brasília') 
        print('BR - De Brasília até Rio de Janeiro') 
        print('RB - Rio de Janeiro até Brasília')
        rota = input(':')
        if rota == 'RS':
            return 1 #Multiplicador da rota RS
        elif rota == 'SR':
            return 1 #Multiplicador da rota SR
        elif rota == 'BS':
            return 1.2 #Multiplicador da rota BS
        elif rota == 'SB':
            return 1.2 #Multiplicador da rota SB
        elif rota == 'BR':
            return 1.5 #Multiplicador da rota BR
        elif rota == 'RB':
            return 1.5 #Multiplicador da rota RB
        else:
            print('**Voce digitou uma rota inexistente')
            print('**Por favor entre com a rota deseja novamente')
            continue
#-----Fim da função rotaObjeto --------

#-----Começo da Main---- 
print('-- Bem-vindo a Companhia de Logistica do Gustavo Menezes Bacelete de Almeida --')
volume = dimensoesObjeto() #Volume final
peso = pesoObjeto() #Peso final
rota = rotaObejto() #Rota final
total = volume * peso * rota #Equação do preço final

print('Total a pagar:R${:.2f} (Dimensões: {} * peso: {} * rota: {}'.format(total, volume, peso, rota))

#-----Fim da Main -------