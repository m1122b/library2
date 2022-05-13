
# app/forms.py


from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField


class BookForm(FlaskForm):
    title = StringField('Tytuł')
    description = TextAreaField('Opis')
    status = SelectField('Status', choices=['', 'wypożyczona', 'niewypożyczona'])


class AuthorForm(FlaskForm):
    firstname = StringField('Imię')
    surname = StringField('Nazwisko')
    book_id = IntegerField('Numer książki')


class BookauthorForm(FlaskForm):
    book_id = IntegerField('Numer książki')
    author_id = IntegerField('Numer autora')


class LoanForm(FlaskForm):
    status = StringField('Status wypożyczenia')
    book_id = IntegerField('Numer książki')


