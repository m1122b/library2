
# app/sqltodos.py


from app import db
from app.models import Book, Author, Bookauthor, Loan


class Todos:
    def allbook(self):
        u = db.session.query(Loan).join(Book).all()
        print('Lista książek')
        for i in u:
            print(i.bookl.title, i.bookl.description, i.status)
        return u
    

    def allauthor(self):
        u = db.session.query(Bookauthor).join(Book, Author).all()
        print('Lista autorów z tytułami')
        for i in u:
            print(i.book_id, i.author_id, i.booka.title, i.author.firstname, i.author.surname)
        return u
    

    def getbook(self, id):
        l = db.session.query(Loan).join(Book).filter(Loan.book_id==id).all()
        mylist = []
        print('Książka')
        for i in l:
            mylist.append(i.bookl.title)
            mylist.append(i.bookl.description)
            mylist.append(i.status)
        return mylist

    
    def getauthor(self, id):
        l = db.session.query(Bookauthor).join(Book, Author).filter(Bookauthor.author_id==id).all()
        mylist = []
        print('Autor')
        for i in l:
            mylist.append(i.author.firstname)
            mylist.append(i.author.surname)
            mylist.append(i.book_id)
        return mylist


    def createbook(self, data):
        data.pop('csrf_token')
        print(data)
        b = Book(title=data['title'], description=data['description'])
        print(b)
        db.session.add(b)
        db.session.commit()
        a = b.id
        print(a)
        l = Loan(status=data['status'], book_id=a)
        print(l)
        db.session.add(l)
        db.session.commit()


    def createauthor(self, data):
        data.pop('csrf_token')
        print(data)
        b = Author(firstname=data['firstname'], surname=data['surname'])
        print(b)
        db.session.add(b)
        db.session.commit()
        a = b.id
        print(a)
        l = Bookauthor(book_id=data['book_id'], author_id=a)
        print(l)
        db.session.add(l)
        db.session.commit()

   
    def updatebook(self, id, data):
        data.pop('csrf_token')
        print(f"id: {id}")
        print(f"data: {data}")
        db.session.query(Book).filter(Book.id == id).update({"title": data['title'], "description": data['description']})
        db.session.query(Loan).filter(Loan.book_id == id).update({"status" : data['status']})
        db.session.commit()    


    def updateauthor(self, id, data):
        data.pop('csrf_token')
        print(f"id: {id}")
        print(f"data: {data}")
        db.session.query(Author).filter(Author.id == id).update({"firstname": data['firstname'], "surname": data['surname']})
        db.session.query(Bookauthor).filter(Bookauthor.author_id == id).update({"book_id" : data['book_id']})
        db.session.commit()


todos = Todos()
