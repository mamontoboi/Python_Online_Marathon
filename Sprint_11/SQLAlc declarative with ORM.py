from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, text
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
book_3.description = u'The theory of evolution'  # update the object >>> book_3 in session # check whether the object is in the session

session.commit()

session.query(Book).order_by(
    Book.id)  # returns a query >>> session.query(Book).order_by(Book.id).all() # returns an object-list
# return all book objects where title == 'The Selfish Gene'
session.query(Book).filter(Book.title == 'The Selfish Gene').order_by(Book.id).all()
# using LIKE
session.query(Book).filter(Book.title.like('The%')).order_by(Book.id).all()
query = session.query(Book).filter(Book.id == 9).order_by(Book.id)
print(query.count())  # returns 0L
print(query.all())  # returns an empty list
print(query.first())  # returns None
print(query.one())  # raises NoResultFound exception
query = session.query(Book).filter(Book.id == 1).order_by(Book.id)
book_1 = query.one()
print(book_1.description)  # returns u'A popular science book'
# book_1.author.books # returns a list of Book-objects representing all the books from the same author.
# get a list of all Book-instances where the author's name is 'Richard Dawkins'
session.query(Book).filter(Book.author_id == Author.id).filter(Author.name == 'Richard Dawkins').all()
session.query(Book).join(Author).filter(Author.name == 'Richard Dawkins').all()
session.query(Book).from_statement(text("SELECT b.* FROM books b, authors a WHERE b.author_id = a.id AND a.name=:name")).\
    params(name='Richard Dawkins').all()
