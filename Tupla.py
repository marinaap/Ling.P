nome_da_tupla1 = (1,2,3)   #Tupla de inteiros
print(nome_da_tupla1)
print(type(nome_da_tupla1))


nome_da_tupla2 = (1, "olá", 1.5) #Tupla heterogênea
print(nome_da_tupla2)

nome_da_tupla3 = ('World', 'teste', 'python')  # tupla de inteiros
print(nome_da_tupla3)


#contando a quantidade de elementos em uma tupla
nome_da_tupla1 = (1,1,2,2,3)
print(nome_da_tupla1.count(2))
print(len(nome_da_tupla1))
print(max(nome_da_tupla1))
print(min(nome_da_tupla1))


# Exibir o indice de uma tupla
nome_da_tupla1 = (10,12,43)  #tupla de inteiros
print(nome_da_tupla1.index(43))

# Verificar a existencia de um elemento dentro da tupla
nome_da_tupla = (1,2,3) #tupla de inteiros
print(2 in nome_da_tupla)
print(22 in nome_da_tupla)