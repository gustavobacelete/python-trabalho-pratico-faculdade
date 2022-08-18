print('--Bem-vindo, esta é a loja de Atacados do Gustavo Menezes--')
#Valor do produto
#Quantidade do produto
#Subtotal do produto
vp = float(input('-Insira o valor do produto:'))
qtd = int(input('-Insira a quantidade desejada do produto:'))
subt = vp * qtd
#Se for menor ou igual a 9 unidades
if qtd <= 9:
    #Não irá receber desconto - menos que 9 unidades
    valorfinal = subt
    print('Poxa, você não recebeu desconto =(')
#Se for igual
elif 10 <= qtd <= 99:
    #Irá receber 5% de desconto - mais de 10 unidades e menos que 100
    valorfinal = subt - subt * 0.05
    print('Parabéns, você recebeu 5% de desconto! =)')
elif 100 <= qtd <= 999:
    #Irá receber 10% de desconto - mais de 100 unidades e menos que 1000
    valorfinal = subt - subt * 0.10
    print('Parabéns, você recebeu 10% de desconto! =)')
else:
    #Irá receber 15% de desconto - mais de 1000 unidades
    valorfinal = subt - subt * 0.15
    print('Parabéns, você recebeu 15% de desconto! =)')
print('O valor do produto sem desconto é de:R${:.2f}'.format(subt))
print('O valor do produto com desconto é de:R${:.2f}'.format(valorfinal))