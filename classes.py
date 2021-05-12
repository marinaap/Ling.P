class Pessoa:
        cpf = 0
        nome = ""
        idade = 0
        telefone = 0
        email = ""
        def falar(self):
            print("Essa pessoa esta falando")
        def andar(self):
            print("Essa pessoa esta andando")
        def comer(self):
            print("Essa pessoa esta comendo")
p1 = Pessoa()
p1.cpf = 123456
p1.nome = "Mari Silva"
p1.idade = 23
p1.telefone = 316664784
p1.email = "maria@ggghh.com"  
p1.andar()  
p1.comer()
p1.falar()

print("CPF", p1.cpf)
print("NOME", p1.nome)
print("IDADE", p1.idade)
print("TELEFONE", p1.telefone)
print("EMAIL", p1.email)

print("\n\n")

p2 = Pessoa()
p2.cpf = 123456
p2.nome = "Jõao Marcelo"
p2.idade = 35
p2.telefone = 319957444
p2.email = "jaom@gmail.com"  
p2.andar()  
p2.comer()
print("CPF", p2.cpf)
print("NOME", p2.nome)
print("IDADE", p2.idade)
print("TELEFONE", p2.telefone)
print("EMAIL", p2.email)