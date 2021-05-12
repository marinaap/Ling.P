#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre qntos dolares ela pode comprar

reais = float(input('Quanto dinheiro voce tem na carteira?  R$ '))
dolar = reais / 5.45 
if reais >= 5.45:
    print('Com R${:.2f} reais será possível comprar U${:.2f} dolares'.format(reais, dolar))
else:
    print('Com R$ {:.2f} não será possivel comprar nem $ 1 dolar!'.format(reais))