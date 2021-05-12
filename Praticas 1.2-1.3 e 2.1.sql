create database if not exists biblioteca
default character set = utf8
default collate = utf8_general_ci;

CREATE TABLE if not exists livros (
id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
titulo VARCHAR(30) NOT NULL DEFAULT'',
autor VARCHAR(25) NOT NULL DEFAULT '',
categoria VARCHAR(25) NOT NULL DEFAULT '',
editora VARCHAR(25) NOT NULL DEFAULT '',
ano_de_publicacao date
);

CREATE TABLE Categoria (
id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
Ficcao_Nao_ficcao VARCHAR(30) NOT NULL DEFAULT '',
Descritores_da_categoria_Area_do_conhecimento VARCHAR(25) NOT NULL DEFAULT ''
);

CREATE TABLE editora (
id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(30) NOT NULL DEFAULT '',
endereco VARCHAR(30) NOT NULL DEFAULT '',
categoria VARCHAR(30) NOT NULL DEFAULT '',
area_do_conhecimento_em_que_atua VARCHAR(30) NOT NULL DEFAULT ''
);

CREATE TABLE autor (
id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(30) NOT NULL DEFAULT '',
pais_de_origem VARCHAR(30) NOT NULL DEFAULT '',
obras_publicadas VARCHAR(30) NOT NULL DEFAULT '',
obras_no_acervo_da_biblioteca VARCHAR(30) NOT NULL DEFAULT ''
);

create database if not exists ornitologia
character set latin1
collate latin1_bin;
show databases;






use ornitologia;
create table passaros(
passaros_id int auto_increment primary key,
nome_cientifico varchar(55) unique,
nome_comum varchar(50),
familia_id int,
descricao text
);
describe passaros;

use biblioteca;
insert into livros(titulo, autor, categoria, editora),
VALUES ('Programação em banco de dados', 'kroton', 'Educacional','Londrina SA');
SELECT * FROM LIVROS
