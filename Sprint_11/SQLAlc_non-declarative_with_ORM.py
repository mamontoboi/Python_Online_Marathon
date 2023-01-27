from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import registry, Session, relationship

# Example is for sqlite. For PostgreSQL do the following:
# 1) In Postgres PgAdmin: CREATE USER redlabxuser WITH PASSWORD 'redlabxpasswd';
# 2) In Postgres PgAdmin: CREATE DATABASE redlabxdb WITH OWNER = redlabxuser;
# 3) In IDE: engine = create_engine('postgresql://redlabxuser:redlabxpasswd@localhost/redlabxdb' , echo=True)
# The string form of the URL is dialect+driver://user:password@host/dbname[?key=value..],
# where dialect is a database name such as mysql, oracle, postgresql, etc.,
# and driver the name of a DBAPI, such as psycopg2, pyodbc, cx_oracle,
# The echo flag is a shortcut to setting up SQLAlchemy logging,
# which is accomplished via Python’s standard logging module.
# With it enabled, we’ll see all the generated SQL produced.


engine = create_engine('sqlite:///library_ORM.db', echo=True)

metadata = MetaData()
mapper_registry = registry()

authors_table = Table('authors', mapper_registry.metadata,
                      Column('id', Integer, primary_key=True),
                      Column('name', String))

books_table = Table('books', mapper_registry.metadata,
                    Column('id', Integer, primary_key=True),
                    Column('title', String),   # Column('name', String(50)) is possible
                    Column('description', String),
                    Column('author_id', ForeignKey('authors.id')))

metadata.create_all(engine)


class Author:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class Book:
    def __init__(self, title, description, author):
        self.title = title
        self.description = description
        self.author = author

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title


mapper_registry.map_imperatively(Book, books_table)
mapper_registry.map_imperatively(Author, authors_table, properties={
    'books': relationship(Book, backref='author')})

session = Session(bind=engine)


session.add(Author(name='George Orwell'))
session.commit()

session.add(Book(title='1984', description='distopia', author=Author(name='George Orwell')))
session.commit()

authors = [Author(name='Kurt Vonnegut'), Author(name='Bel Kaufman')]
for i in authors:
    session.add(i)

session.add_all([Book(title='Slaughterhouse Five', description='anti-war novel', author=Author(name='Kurt Vonnegut')),
                 Book(title="Cat's cradle", description='anti-war novel', author=Author(name='Kurt Vonnegut')),
                 Book(title='Up the down staircase', description='comedy, youth prose',
                      author=Author(name='Bel Kaufman'))])

session.commit()

# To check all entries
data_from_db = session.query(Author).all()
for row in data_from_db:
    print(row)

# To find specific entry
data = session.query(Book).filter(Book.title == "Cat's cradle").order_by(Book.id).all()
for row in data:
    print(row)

# # To delete all users Kurt Vonnegut
session.execute(authors_table.delete().where(authors_table.c.name == "Kurt Vonnegut"))
session.commit()
#
# # To delete all
# session.execute(authors_table.delete())
# session.commit()
