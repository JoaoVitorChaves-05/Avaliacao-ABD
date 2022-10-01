CREATE DATABASE avaliacao_abd;

USE avaliacao_abd;

CREATE TABLE campeonato (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    nome_campeonato VARCHAR(255) NOT NULL,
    n_max_times INTEGER NOT NULL
);

CREATE TABLE cidade (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    nome_cidade VARCHAR(255) NOT NULL
);

CREATE TABLE estadio (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    nome_estadio VARCHAR(255) NOT NULL,
    capacidade INTEGER NOT NULL,
    id_cidade INTEGER NOT NULL,
    FOREIGN KEY (id_cidade) REFERENCES cidade(id)
);

CREATE TABLE time_futebol (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    nome_time VARCHAR(255) NOT NULL,
    id_cidade INTEGER NOT NULL,
    id_estadio INTEGER NOT NULL,
    FOREIGN KEY (id_estadio) REFERENCES estadio(id),
    FOREIGN KEY (id_cidade) REFERENCES cidade(id)
);

CREATE TABLE jogador (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    nome_jogador VARCHAR(255) NOT NULL,
    id_time INTEGER NOT NULL,
    FOREIGN KEY (id_time) REFERENCES time_futebol(id)
);

CREATE TABLE treinador (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    nome_treinador VARCHAR(255) NOT NULL,
    id_time INTEGER NOT NULL,
    FOREIGN KEY (id_time) REFERENCES time_futebol(id)
);

CREATE TABLE time_campeonato (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    id_time INTEGER NOT NULL,
    id_campeonato INTEGER NOT NULL,
    pontos INTEGER NOT NULL,
    FOREIGN KEY (id_campeonato) REFERENCES campeonato(id)
);

CREATE TABLE jogo (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    id_time_visitante INTEGER NOT NULL,
    id_time_mandante INTEGER NOT NULL,
    data_jogo TIMESTAMP,
    id_estadio INTEGER,
    id_campeonato INTEGER,
    FOREIGN KEY (id_time_visitante) REFERENCES time_futebol(id),
    FOREIGN KEY (id_time_mandante) REFERENCES time_futebol(id),
    FOREIGN KEY (id_estadio) REFERENCES estadio(id),
    FOREIGN KEY (id_campeonato) REFERENCES campeonato(id)
);