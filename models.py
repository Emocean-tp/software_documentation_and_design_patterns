from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Movie(Base):
    __tablename__ = 'movies'

    movieID = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    releaseYear = Column(Integer)
    genre = Column(String)

    actors = relationship("MovieActor", back_populates="movie")
    reviews = relationship("Review", back_populates="movie")
    ratings = relationship("Rating", back_populates="movie")
    facts = relationship("Fact", back_populates="movie")
    boxOffice = relationship("BoxOffice", back_populates="movie")


class Actor(Base):
    __tablename__ = 'actors'

    actorID = Column(Integer, primary_key=True)
    firstName = Column(String)
    lastName = Column(String)

    movies = relationship("MovieActor", back_populates="actor")


class MovieActor(Base):
    __tablename__ = 'movie_actors'

    movieActorID = Column(Integer, primary_key=True)

    movieID = Column(Integer, ForeignKey('movies.movieID'))
    actorID = Column(Integer, ForeignKey('actors.actorID'))

    roleName = Column(String)

    movie = relationship("Movie", back_populates="actors")
    actor = relationship("Actor", back_populates="movies")


class Review(Base):
    __tablename__ = 'reviews'

    reviewID = Column(Integer, primary_key=True)

    movieID = Column(Integer, ForeignKey('movies.movieID'))

    criticName = Column(String)
    comment = Column(String)

    movie = relationship("Movie", back_populates="reviews")


class Rating(Base):
    __tablename__ = 'ratings'

    ratingID = Column(Integer, primary_key=True)

    movieID = Column(Integer, ForeignKey('movies.movieID'))

    criticName = Column(String)
    score = Column(Float)

    movie = relationship("Movie", back_populates="ratings")


class Fact(Base):
    __tablename__ = 'facts'

    factID = Column(Integer, primary_key=True)

    movieID = Column(Integer, ForeignKey('movies.movieID'))

    factText = Column(String)

    movie = relationship("Movie", back_populates="facts")


class BoxOffice(Base):
    __tablename__ = 'box_office'

    boxOfficeID = Column(Integer, primary_key=True)

    movieID = Column(Integer, ForeignKey('movies.movieID'))

    budget = Column(Float)
    worldwideGross = Column(Float)

    movie = relationship("Movie", back_populates="boxOffice")