#Desenvolva um programa que leia duas notas de uma aluno, calcule e mostre a sua média
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
soma = nota1 + nota2
media = soma / 2
print('A média das notas é:{:.f1}'.format(media))  #  (:.f1 significa depois do ponto flutuante vem 1 numero)

