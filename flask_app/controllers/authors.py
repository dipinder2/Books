from flask import Flask, render_template,request,redirect
from flask_app import app
from ..models import author
from ..models.book import Book
from ..models.favorite import Favorite
@app.route('/')
def index():
    authors = author.Author.get_all()
    return render_template("index.html", authors = authors)


@app.route('/add/author', methods=['GET', 'POST'])
def add_user():
    author.Author.add_one(request.form)
    return redirect('/')


@app.route('/author/<int:id>')
def show_author(id):
    return render_template('authorshow.html', author = author.Author.get_one({'id':id}), books = Book.get_all())


@app.route('/author/favorites',methods=['POST'])
def add_author_favorites():
    Favorite.add_one({
        "author_id":int(request.form['author_id']),
        "book_id":int(request.form['book_id'])})
    return redirect(f'/author/{request.form["author_id"]}')