from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import relationship, backref, Session
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine('sqlite:///library_Decl.db', echo=True)


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship(Author, backref=backref('books', order_by=title))

    def __init__(self, title, description, author):
        self.title = title
        self.description = description
        self.author = author

    def __repr__(self):
        return self.title


Base.metadata.create_all(engine)

session = Session(bind=engine)

author_1 = Author('Richard Dawkins')
author_2 = Author('Matt Ridley')
book_1 = Book('The Red Queen', 'A popular science book', author_2)
book_2 = Book('The Selfish Gene', 'A popular science book', author_1)
book_3 = Book('The Blind Watchmaker', 'The theory of evolution', author_1)
session.add(author_1)
session.add(author_2)
session.add_all([book_1, book_2, book_3])
session.commit()
book_3.description = u'The theory of evolution' # update the object >>> book_3 in session # check whether the object is in the session

session.commit()