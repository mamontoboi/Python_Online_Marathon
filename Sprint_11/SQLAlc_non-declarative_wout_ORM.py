from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, select

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

engine = create_engine('sqlite:///library.db', echo=True)
metadata = MetaData()
authors_table = Table('authors', metadata,
                      Column('id', Integer, primary_key=True),
                      Column('name', String))

books_table = Table('books', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('title', String),   # Column('name', String(50)) is possible
                    Column('description', String),
                    Column('author_id', ForeignKey('authors.id')))

metadata.create_all(engine)  # creates the tables

conn = engine.connect()  # creates connection

conn.execute(authors_table.insert().values(name='John Smith'))  # Execute the insert query
conn.execute(authors_table.insert().values([{'name': 'Mr X'}, {'name': 'Mr Y'}]))  # a list of entries
conn.commit()  # save into DB

# To check all entries
data_from_db = conn.execute(select(authors_table)).fetchall()
for row in data_from_db:
    print(row)

# To find specific entry
select_stmt = conn.execute(authors_table.select().where(authors_table.c.id == 2)).fetchone()
print(select_stmt)


# To delete specific line, with id = 2
del_num_2 = authors_table.delete().where(authors_table.c.id == 2)
conn.execute(del_num_2)
conn.commit()


# To delete all users X
conn.execute(authors_table.delete().where(authors_table.c.name == "Mr X"))
conn.commit()

# To delete all
conn.execute(authors_table.delete())
conn.commit()
