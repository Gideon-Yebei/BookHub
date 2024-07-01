import os

class Config:
	SECRET_KEY = os.urandom(24)
	BASE_DIR = os.path.abspath(os.path.dirname(__file__))
	DATABASE_PATH = os.path.normpath(os.path.join(BASE_DIR, '..', 'database', 'bookhub.db'))
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
	print(SQLALCHEMY_DATABASE_URI)  # Temporary print statement to verify the path
	SQLALCHEMY_TRACK_MODIFICATIONS = False
