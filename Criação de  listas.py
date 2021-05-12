# Criação de uma lista vazia
lista_vazia = []
# Criacao de uma lista de inteiros
lista_inteiros = [1,2,3,8,14,4,5]
# Criacao de uma lista de Strings
lista_string = ["olá mundo"]
#criação de uma lista booleana
lista_booleana = [True, False, False, True]
# Criacao de uma lista com varios tipos diferentes
lista_tipos = [1,"olá mundo!",1.5, True]
# listas dentro de outra lista. estas sao chamadas nested lists:
lista_lista = ["olá mundo", [1,2,3],["outra lista"]]
print(lista_vazia)
print(lista_inteiros)
print(lista_tipos)
print(lista_booleana)
print(lista_string)
print(lista_lista)

#inserindo elementos na lista
# A inserção de elementos em uma lista pode ser feita por dois metodos,
# O append()  e o insert().
# o metodo append() insere o elemento SEMPRE NO FINAL DA LISTA,
# o metodo insert() irá inserir o elemneto numa posição especifica,


lista = []
lista.append(2)    #posição 0
lista.append(3)    #posição 1
lista.append(12)   #posição 2
lista.append(8)    #posição 3
lista.insert(0,44) #posição 4
lista.insert(2,6)  #posição 4
print(lista)

#exemplo_lista1 = [2,2,4,18,1,7,5]


lista = []
lista.append(2)    #posição 0
lista.append(3)    #posição 1
lista.append(12)   #posição 2
lista.append(8)    #posição 3

lista.insert(2,6)  
print(lista)



# tamanho da lista
# Len()
from typing import Counter


lista_len = [3,4,5,6,7]
print(len(lista_len))

lista_len2 = ["3,4,5,6,7"]
print(len(lista_len2))

Listaaula5 = []
Listaaula5.append(0)
Listaaula5.append(1)
Listaaula5.append(2)
Listaaula5.insert(2,3)
Listaaula5.insert(0,5)
print(Listaaula5)

bolo = ['farinha de trigo', 'ovo', 'leite', 'manteiga']
bolo.append(['açucar', 'fermento'])
print(bolo)

s = list("Ordem e Progresso")
print(s)

# Converte uma lista em uma string.
l = ['O', 'r', 'd', 'e', 'm', ' ', 'e', ' ', 'P', 'r', 'o', 'g', 'r', 'e', 's', 's', 'o']
print(''.join(l))

# JUNTANDO LISTAS
m = [1, 25, 13]
n = [44, 51, 16]
o = m + n
print(o) # [1, 2, 3, 4, 5, 6]


ex_lista1 = [0,1,2,3,4,5,6]


intervalo = slice(1,4) # cortar a lista a partir da posiçãao 1 até a posicção quatro
print(ex_lista1[intervalo])

# UTILIZANDO LIST COMPREHENSION
s = [x+1 for x in range(5)]
print(s)


#UTILIZANDO Count() CONTA QNTOS ELEMENTOS 6 EXISTEM NA LISTA
lista1 = [0,1,2,3,4,5,6]
x=lista1.count(6)
print(x)

lista_conta_palavra = ["python", "ola", "python","ola"]
palavra = lista_conta_palavra.count ("python")
print(palavra)


# Sintaxe da função range().
inicio = 0
fim = 100
passo = 10
#Convertendo um intervalo em uma lista.
print(list(range(inicio, fim, passo)))

