CREATE TABLE Users(
    idUser CHAR(36) PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL,
    password TEXT NOT NULL,
    salt VARCHAR(28) NOT NULL,
    profilPicture TEXT,
    abonnementType INT NOT NULL,
    RegisterAt DATE NOT NULL,
    BuyAPremiumAt DATE,
    artistInfo CHAR(36),
    FOREIGN KEY (abonnementType) REFERENCES Abonnements(idAbonnement),
    FOREIGN KEY (artistInfo) REFERENCES Artist(idArtist)
) ENGINE=InnoDB;

CREATE TABLE Abonnements(
    idAbonnement INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
) ENGINE=InnoDB;

CREATE TABLE Artist(
    idArtist CHAR(36) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    MonthlyAuditor INT
) ENGINE=InnoDB;

CREATE TABLE Music(
    idMusic CHAR(36) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    artistId CHAR(36) NOT NULL,
    coverImage LONGBLOB,
    isExplicit BOOLEAN,
    musicLenghtSecond FLOAT NOT NULL,
    FOREIGN KEY (artistId) REFERENCES Artist(idArtist)
) ENGINE=InnoDB;

CREATE TABLE ArtistSubscriptions(
    idArtistSubscriptions CHAR(36) PRIMARY KEY,
    idUser CHAR(36) NOT NULL,
    idArtist CHAR(36) NOT NULL,
    FOREIGN KEY (idUser) REFERENCES Users(idUser),
    FOREIGN KEY (idArtist) REFERENCES Artist(idArtist)
) ENGINE=InnoDB;

CREATE TABLE UserLikedMusic(
    idUser CHAR(36) NOT NULL,
    idMusic CHAR(36) NOT NULL,
    likedAt DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (idUser, idMusic),
    FOREIGN KEY (idUser) REFERENCES Users(idUser),
    FOREIGN KEY (idMusic) REFERENCES Music(idMusic)
) ENGINE=InnoDB;
