
# app/models.py


from app import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(300))
    bookauthors = db.relationship("Bookauthor", backref="booka", lazy="dynamic")
    loan = db.relationship('Loan', backref='bookl')

    def __str__(self):
        return f"<Book {self.title} {self.description}>"


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100))
    surname = db.Column(db.String(100))
    bookauthors = db.relationship("Bookauthor", backref="author", lazy="dynamic")

    def __str__(self):
        return f"<Author {self.surname}>"


class Bookauthor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))

    def __str__(self):
        return f"<Bookauthor {self.book_id} {self.author_id}>"


class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(100))
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    
    def __str__(self):
        return f"<Loan {self.book_id} {self.status}>"


