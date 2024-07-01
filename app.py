from flask import Flask, render_template
from extensions import db

app = Flask(__name__)
app.config.from_object('configs.config.Config')
db.init_app(app)

# Import models after db is initialized with app
from models.models import User, Book, Favorite, Review

@app.route('/')
def index():
    recommended_books = Book.query.all()
    return render_template('index.html', recommended_books=recommended_books)

@app.route('/book/<int:book_id>')
def book_details(book_id):
    book = Book.query.get(book_id)
    return render_template('book_details.html', book=book)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
