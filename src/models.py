import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()



class Character(Base):
    __tablename__ = "character"
    character_id = Column(Integer, primary_key=True)
    gender = Column(String(40))
    name = Column(String(40), unique=True, nullable=False)
    film_id = Column(Integer, nullable=False)
    homeworld_id = Column(Integer, nullable=False)
    vehicle_id = Column(Integer, nullable=False)

class Planet(Base):
    __tablename__ = "planet"
    planet_id = Column(Integer, primary_key=True)
    climate = Column(String(200))
    gravity = Column(String(200))
    name = Column(String(40), nullable=False)
    resident_id = Column(Integer,ForeignKey('character.character_id') ,nullable=False)
    character= relationship(Character)
    film_id = Column(Integer,nullable=False)



class User(Base):
    __tablename__ = "user"
    user_id = Column(Integer, primary_key=True)
    user_name = Column (String(40), unique=True, nullable=False)
    user_password = Column (String(40), nullable=False)
    email = Column (String (49), unique=True, nullable=False)

class FavoritePlanets(Base):
    __tablename__ = 'fav_planet'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    user = relationship(User)

class FavoriteCharacters(Base):
    __tablename__ = 'fav_character'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user.id'))
    character_id = Column(Integer, ForeignKey('character.character.id'))
    user = relationship(User)

class FavoriteFilm(Base):
    __tablename__ = 'fav_character'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user.id'))
    film_id = Column(Integer, ForeignKey('film.film.id'))
    user = relationship(User)

class Film(Base):
    __tablename__ = "film"
    film_id = Column(Integer, primary_key=True)
    character_id = Column(Integer,ForeignKey('character.character_id') ,nullable=False)
    character = relationship(Character)
    planet_id = Column(Integer, ForeignKey('planet.planet_id') ,nullable=False)
    planet = relationship(Planet)
    director = Column(String(40), nullable=False)
    producer = Column(String(40), nullable=False)
    title = Column(String(200), nullable=False)

    
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
