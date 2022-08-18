print('Seja bem-vindo a lanchonete do Gustavo Menezes Bacelete de Almeida')
print('----------------Cardápio------------------')
print('__________________________________________')
print('Código |        Descrição      | Valor(R$)')
print('------------------------------------------')
print('  100  |     Cachorro-Quente   |     9,00')
print('  101  | Cachorro-Quente Duplo |    11,00')
print('  102  |         X-Egg         |    12,00')
print('  103  |        X-Salada       |    13,00')
print('  104  |        X-Bacon        |    14,00')
print('  105  |         X-Tudo        |    17,00')
print('  200  |    Refrigerante Lata  |     5,00')
print('  201  |        Chá Gelado     |     4,00')
print('------------------------------------------')
subtotal = 0 #Valor do pedido
while True:
    codigo = int(input('Digite o código do produto desejado:'))
#Quando o usuario escolher algum produto, automaticamente vai adicionar o valor no subtotal.
    if codigo == 100:
        print('Você pediu um Cachorro-Quente no valor de R$9,00.')#Produto que foi pedido
        subtotal = subtotal + 9 #Subtotal vai guardar o valor dos pedidos 
    elif codigo == 101:
        print('Você pediu um Cachorro-Quente Duplo no valor de R$11,00.')
        subtotal = subtotal + 11
    elif codigo == 102:
        print('Você pediu um X-Egg no valor de R$12,00.')
        subtotal = subtotal + 12
    elif codigo == 103:
        print('Você pediu um X-Salada no valor de R$13,00.')
        subtotal = subtotal + 13
    elif codigo == 104:
        print('Você pediu um X-Bacon no valor de R$14,00.')
        subtotal = subtotal + 14
    elif codigo == 105:
        print('Você pediu um X-Tudo no valor de R$17,00.')
        subtotal = subtotal + 17
    elif codigo == 200:
        print('Você pediu um Refrigerante Lata no valor de R$5,00.')
        subtotal = subtotal + 5
    elif codigo == 201:
        print('Você pediu um Chá Gelado no valor de R$4,00.')
        subtotal = subtotal + 4
    else: #Caso o usuario digite um código que não está no cardápio.
        print('Produto inexistente. Digite outro código.')
        continue
    print('Valor do pedido no momento:R${:.2f}'.format(subtotal))#Subtotal no momento
    resposta = input('Deseja pedir mais alguma coisa?\n 1 - Sim \n 0 - Não')
    if resposta == '1':#Se o usuario digitar 1 o programa irá prosseguir com o pedido
        continue
    else:#Se o usuario digitar 0 o outra coisa o programa será encerrado e o total a ser pago imprimido.
        print('Total a ser pago: R${:.2f}'.format(subtotal))#Valor final de tudo
        break
    