# Questão 1
# Crie uma lista vazia. Peça ao usuário para digitar 5 números inteiros e
# armazene-os na Lista. Agora retire um numero qualquer usando uma
# função. Insira o elemento na lista. Percorra essa lista e imprima os seus
# elementos na tela.

list = []
n1 = int(input('Digite o 1º num:  '))
n2 = int(input('Digite o 2º num:  '))
n3 = int(input('Digite o 3º num:  '))
n4 = int(input('Digite o 4º num:  '))
n5 = int(input('Digite o 5º num:  '))
list = [n1,n2,n3,n4,n5]
list.pop(2)
print(list)
list.insert(2,5)
print(list)
for list in list:
    print(list)


