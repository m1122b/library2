
# library.py


from app import app, db
from flask import Flask, request, render_template, redirect, url_for, abort, make_response, jsonify
from app.models import Book, Bookauthor, Author, Loan
from app.forms import BookForm, AuthorForm, BookauthorForm, LoanForm
from app.sqltodos import todos


@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "Book": Book,
        "Author": Author,
        "Bookauthor" : Bookauthor,
        "Loan" : Loan
    }


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found', 'status_code': 404}), 404)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request', 'status_code': 400}), 400)


@app.route("/", methods=["GET", "POST"])
def books_list():
    bookform = BookForm()
    authorform = AuthorForm()
    bookauthorform = BookauthorForm()
    loanform = LoanForm()
    error = ""
    return render_template("books.html", bookform=bookform, authorform=authorform, bookauthorform=bookauthorform, loanform=loanform, allbook=todos.allbook(), allauthor=todos.allauthor(), error=error)


@app.route("/addbook/", methods=["GET", "POST"])
def addbook():
    bookform = BookForm()
    error = ""
    if request.method == "POST":
        if bookform.validate_on_submit():
            todos.createbook(bookform.data)
        return redirect(url_for("books_list"))
    
    return render_template("addbook.html", bookform=bookform, error=error)


@app.route("/addauthor/", methods=["GET", "POST"])
def addauthor():
    authorform = AuthorForm()
    error = ""
    if request.method == "POST":
        if authorform.validate_on_submit():
            todos.createauthor(authorform.data)
        return redirect(url_for("books_list"))
    
    return render_template("addauthor.html", authorform=authorform, error=error)


@app.route("/book/<int:todo_id>/", methods=["GET", "POST"])
def book_details(todo_id):
    todo = todos.getbook(todo_id)
    print(type(todo))
    todo1 = ('title' , 'description' , 'status')
    todo_dict = dict(zip(todo1, todo))
    print(todo_dict)
    form = BookForm(data=todo_dict)
    if request.method == "POST":
        if form.validate_on_submit():
            todos.updatebook(todo_id, form.data)
        return redirect(url_for("books_list"))
    return render_template("book.html", form=form, todo_id=todo_id)


@app.route("/author/<int:todo_id>/", methods=["GET", "POST"])
def author_details(todo_id):
    todo = todos.getauthor(todo_id)
    print(type(todo))
    todo1 = ('firstname' , 'surname' , 'book_id')
    todo_dict = dict(zip(todo1, todo))
    print(todo_dict)
    form = AuthorForm(data=todo_dict)
    if request.method == "POST":
        if form.validate_on_submit():
            todos.updateauthor(todo_id, form.data)
        return redirect(url_for("books_list"))
    return render_template("author.html", form=form, todo_id=todo_id)




if __name__ == "__main__":
    
    app.run(debug=True)


