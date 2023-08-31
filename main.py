# database uri : define 
# session maker : handling session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from models.book import Book
from models.author import Author
from models.base import Base 

# creating the db
DATABASE_URI = "sqlite:///publisherlist.db"
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

# creating the tables 
Base.metadata.create_all(engine)  

# creating authors and books 
authorName = "Joseph"
bookTitle = "ABC Book"

authorName2 = "Mary"
bookTitle2 = "DEF Book"
# utilising a helper method
# validate / assumpation handling 
# object creation / record insert to the db table 
author1 = session.query(Author).filter_by(name=authorName).first()
if not author1:
    author1 = Author(name=authorName)

book1 = session.query(Book).filter_by(title=bookTitle).first()
if not book1:
    book1 = Book(title=bookTitle)

book2 = session.query(Book).filter_by(title=bookTitle2).first()
if not book2:
    book2 = Book(title=bookTitle2)

# helper 
book1.add_author(author1)
book2.add_author(author1)

# adding objects to session 
if author1 not in session:
    session.add(author1)
if book1 not in session:
   session.add(book1)
if book2 not in session:
   session.add(book2)

session.commit()

# READ 
all_authors = session.query(Author).all()
for author in all_authors:
    print("Author name: ", author.name)
    for book in author.books:
        print("-Book: " , book.title)

# Update 
authortoUpdate = session.query(Author).filter_by(name=authorName2).first()
if authortoUpdate:
    authortoUpdate.name = "Alice"
    session.commit()


#  TODO : CHECK WHY THE ERROR ON DELETE INVOLVES THE JOIN TABLE.
# delete data : delete data that also belongs to associations ??/ 
# authortoDelete = session.query(Author).filter_by(name=authorName).first()
# if authortoDelete: 
#     session.delete(authortoDelete)
#     session.commit()
# else:
#     print("Author not found, unable to delete")

# close the session 
session.close()