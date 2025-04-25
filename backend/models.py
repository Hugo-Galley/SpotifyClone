from typing import List, Optional

from sqlalchemy import CHAR, Date, DateTime, Float, ForeignKeyConstraint, Index, String, Text, text
from sqlalchemy.dialects.mysql import INTEGER, LONGBLOB, TINYINT
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()


class Abonnements(Base):
    __tablename__ = 'Abonnements'

    idAbonnement: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(255))

    Users: Mapped[List['Users']] = relationship('Users', back_populates='Abonnements_')


class Artist(Base):
    __tablename__ = 'Artist'

    idArtist: Mapped[str] = mapped_column(CHAR(36), primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    MonthlyAuditor: Mapped[Optional[int]] = mapped_column(INTEGER(11))

    Music: Mapped[List['Music']] = relationship('Music', back_populates='Artist_')
    Users: Mapped[List['Users']] = relationship('Users', back_populates='Artist_')
    ArtistSubscriptions: Mapped[List['ArtistSubscriptions']] = relationship('ArtistSubscriptions', back_populates='Artist_')


class Music(Base):
    __tablename__ = 'Music'
    __table_args__ = (
        ForeignKeyConstraint(['artistId'], ['Artist.idArtist'], name='music_ibfk_1'),
        Index('artistId', 'artistId')
    )

    idMusic: Mapped[str] = mapped_column(CHAR(36), primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    artistId: Mapped[str] = mapped_column(CHAR(36))
    musicLenghtSecond: Mapped[float] = mapped_column(Float)
    coverImage: Mapped[Optional[bytes]] = mapped_column(LONGBLOB)
    isExplicit: Mapped[Optional[int]] = mapped_column(TINYINT(1))

    Artist_: Mapped['Artist'] = relationship('Artist', back_populates='Music')
    UserLikedMusic: Mapped[List['UserLikedMusic']] = relationship('UserLikedMusic', back_populates='Music_')


class Users(Base):
    __tablename__ = 'Users'
    __table_args__ = (
        ForeignKeyConstraint(['abonnementType'], ['Abonnements.idAbonnement'], name='users_ibfk_1'),
        ForeignKeyConstraint(['artistInfo'], ['Artist.idArtist'], name='users_ibfk_2'),
        Index('abonnementType', 'abonnementType'),
        Index('artistInfo', 'artistInfo')
    )

    idUser: Mapped[str] = mapped_column(CHAR(36), primary_key=True)
    email: Mapped[str] = mapped_column(String(255))
    username: Mapped[str] = mapped_column(String(255))
    password: Mapped[str] = mapped_column(Text)
    salt: Mapped[str] = mapped_column(String(28))
    abonnementType: Mapped[int] = mapped_column(INTEGER(11))
    RegisterAt: Mapped[datetime.date] = mapped_column(Date)
    profilPicture: Mapped[Optional[str]] = mapped_column(Text)
    BuyAPremiumAt: Mapped[Optional[datetime.date]] = mapped_column(Date)
    artistInfo: Mapped[Optional[str]] = mapped_column(CHAR(36))

    Abonnements_: Mapped['Abonnements'] = relationship('Abonnements', back_populates='Users')
    Artist_: Mapped[Optional['Artist']] = relationship('Artist', back_populates='Users')
    ArtistSubscriptions: Mapped[List['ArtistSubscriptions']] = relationship('ArtistSubscriptions', back_populates='Users_')
    UserLikedMusic: Mapped[List['UserLikedMusic']] = relationship('UserLikedMusic', back_populates='Users_')


class ArtistSubscriptions(Base):
    __tablename__ = 'ArtistSubscriptions'
    __table_args__ = (
        ForeignKeyConstraint(['idArtist'], ['Artist.idArtist'], name='artistsubscriptions_ibfk_2'),
        ForeignKeyConstraint(['idUser'], ['Users.idUser'], name='artistsubscriptions_ibfk_1'),
        Index('idArtist', 'idArtist'),
        Index('idUser', 'idUser')
    )

    idArtistSubscriptions: Mapped[str] = mapped_column(CHAR(36), primary_key=True)
    idUser: Mapped[str] = mapped_column(CHAR(36))
    idArtist: Mapped[str] = mapped_column(CHAR(36))

    Artist_: Mapped['Artist'] = relationship('Artist', back_populates='ArtistSubscriptions')
    Users_: Mapped['Users'] = relationship('Users', back_populates='ArtistSubscriptions')


class UserLikedMusic(Base):
    __tablename__ = 'UserLikedMusic'
    __table_args__ = (
        ForeignKeyConstraint(['idMusic'], ['Music.idMusic'], name='userlikedmusic_ibfk_2'),
        ForeignKeyConstraint(['idUser'], ['Users.idUser'], name='userlikedmusic_ibfk_1'),
        Index('idMusic', 'idMusic')
    )

    idUser: Mapped[str] = mapped_column(CHAR(36), primary_key=True)
    idMusic: Mapped[str] = mapped_column(CHAR(36), primary_key=True)
    likedAt: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))

    Music_: Mapped['Music'] = relationship('Music', back_populates='UserLikedMusic')
    Users_: Mapped['Users'] = relationship('Users', back_populates='UserLikedMusic')
