SET AUTOCOMMIT=0;
CREATE TABLE Marca(
Id INT PRIMARY KEY AUTO_INCREMENT,
Nome VARCHAR(30) NOT NULL
);
INSERT Marca VALUES (0, "Marca_A"),
(0, "Marca_B"),
(0, "Marca_C");

CREATE TABLE Peca(
Num INT PRIMARY KEY AUTO_INCREMENT,
Nome VARCHAR(30) NOT NULL,
Preco DECIMAL(6,2) NOT NULL,
MarcaId INT NOT NULL,
FOREIGN KEY(MarcaId) REFERENCES Marca(Id)
);
INSERT Peca values 
(0, "Espelho", "50.00", 1),
(0, "Espelho", "40.00", 2),
(0, "Transmissao", "150.00", 1),
(0, "Transmissao", "250.00", 2),
(0, "Transmissao", "170.00", 3),
(0, "Cabo do acelerador", "100.00", 2),
(0, "Cabo do acelerador", "80.00", 3),
(0, "Lampada dianteira", "10.00", 1),
(0, "Lampada dianteira", "10.00", 2),
(0, "Lampada dianteira", "15.00", 3),
(0, "Cabo de freio", "75.00", 1);
SAVEPOINT pontoMoto;
INSERT Marca values(0, "Marca_Z");
UPDATE Peca SET MarcaId = 4 WHERE MarcaId = 3;
DELETE FROM Peca WHERE Num = 10 AND Preco = 15.00;
ROLLBACK TO SAVEPOINT pontoMoto;
COMMIT;
INSERT peca values (0, "Lampada dianteira", "15.00", 3),
SELECT Peca.Nome AS "Peça", Peca.Preco AS "Preço", Marca.Nome AS "Marca"
FROM Peca INNER JOIN Marca
ON Peca.MarcaId = Marca.Id;
 
DROP table marcas;
