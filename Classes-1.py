class Computador:
    marca =  ""
ram = ""
hd = ""
monitor = ""
def funciona(self):
    print("Sim")

pc1 = Computador()
pc1.marca = "del"
pc1.ram = "16g"
pc1.hd = "1 tera"
pc1.monitor = "17 polegadas"
print("Marca",pc1.marca)
print("Memoria", pc1.ram)
print("HD", pc1.hd)
print("Monitor", pc1.monitor)
print("\n\n")

pc2 = Computador()
pc2.marca = "CCE"
pc2.ram = "8gb"
pc2.hd = "500g"
pc2.monitor = "14 polegadas"

print("Marca",pc2.marca)
print("Memoria", pc2.ram)
print("HD", pc2.hd)
print("Monitor", pc2.monitor)

