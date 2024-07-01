from extensions import db

class User(db.Model):
	__tablename__ = 'users'  # Specify table name
	def __init__(self, username, password):
		self.username = username
		self.password = password
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(150), unique=True, nullable=False)
	password = db.Column(db.String(150), nullable=False)
	favorites = db.relationship('Favorite', backref='user', lazy=True)
	reviews = db.relationship('Review', backref='user', lazy=True)

class Book(db.Model):
	__tablename__ = 'books'  # Specify table name
	def __init__(self, title='', author='', genre='', description=''):
		self.title = title
		self.author = author
		self.genre = genre
		self.description = description
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(200), nullable=False)
	author = db.Column(db.String(150), nullable=False)
	genre = db.Column(db.String(100), nullable=False)
	description = db.Column(db.Text, nullable=True)
	reviews = db.relationship('Review', backref='book', lazy=True)
	favorites = db.relationship('Favorite', backref='book', lazy=True)

class Favorite(db.Model):
	__tablename__ = 'favorites'  # Specify table name
	def __init__(self, user, book):
		self.user = user
		self.book = book

	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Adjust foreign key reference
	book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)  # Adjust foreign key reference

class Review(db.Model):
	__tablename__ = 'reviews'  # Specify table name
	def __init__(self, user, book, rating, comment=''):
		self.user = user
		self.book = book
		self.rating = rating
		self.comment = comment

	id = db.Column(db.Integer, primary_key=True)
	book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)  # Adjust foreign key reference
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Adjust foreign key reference
	rating = db.Column(db.Integer, nullable=False)
	comment = db.Column(db.Text, nullable=True)
