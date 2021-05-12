create table receitas(
Prato varchar(30) not null,
Tempo int not null,
Ingredientes varchar(200) not null
);

insert receitas values ("Yakssoba", 40, "espaguete, cebola, óleo, brócolis, couve-flor,
molho de soja, carne, cenoura, acelga"),
("strogonoff de carne", 30, "carne, cebola, champignon, creme de leite, tomates,
ketchup, mostrada, caldo de carne"),
("Pão Caseiro 1", 60, "ovo, açúcar, sal, agua, óleo, fermento seco, farinha trigo"),
("Pão Caseiro 2", 60, "ovo, leite, fermento biologico, margarina, sal, açúcar, farinha
de trigo"),
("Lasanha", 50, "massa de lasanha, carne moída, presunto, mussarela, cebola, óleo,
molho de tomate, queijo ralado"),
("Filé ao molho madeira", 30, "filé mignon, champignon, manteiga, cebola, caldo de
carne, vinho tinto seco, amido de milho"),
("Filé de peixe com alcaparras", 20, "filé de peixe, Sal, Pimenta do reino, limão,
azeite, alcaparra");
ALTER TABLE receitas ADD FULLTEXT(Ingredientes);
SELECT Prato
FROM receitas
WHERE Ingredientes not in (select Ingredientes from receitas where MATCH(Ingredientes)
AGAINST("leite, queijo, requeijão, iogurte"));