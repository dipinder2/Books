from flask import redirect, render_template,request
from flask_app import app
from ..models.book import Book
from ..models.author import Author
from ..models.favorite import Favorite

@app.route('/books')
def books():
    return render_template('books.html',books = Book.get_all())


@app.route('/add/book', methods=['POST'])
def add_books():
    Book.add_one(request.form)
    return redirect('/books')


@app.route('/book/<int:id>')
def show_book(id):
    return render_template('bookshow.html', book = Book.get_one({'id':id}), authors = Author.get_all())


@app.route('/book/favorites',methods=['POST'])
def add_book_favorites():
    print(request.form)
    Favorite.add_one({
        "author_id":int(request.form['author_id']),
        "book_id":int(request.form['book_id'])})
    return redirect(f'/book/{request.form["book_id"]}')