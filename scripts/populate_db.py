import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('database/bookhub.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        genre TEXT NOT NULL,
        description TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS favorites (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        book_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (id),
        FOREIGN KEY (book_id) REFERENCES books (id)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        book_id INTEGER NOT NULL,
        rating INTEGER NOT NULL,
        comment TEXT,
        FOREIGN KEY (user_id) REFERENCES users (id),
        FOREIGN KEY (book_id) REFERENCES books (id)
    )
''')

# Insert data into tables
cursor.execute('''
    INSERT INTO users (username, password) VALUES
    ('alice', 'password123'),
    ('bob', 'password123')
''')

cursor.execute('''
    INSERT INTO books (title, author, genre, description) VALUES
    ('The Great Gatsby', 'F. Scott Fitzgerald', 'Fiction', 'A novel set in the 1920s...'),
    ('To Kill a Mockingbird', 'Harper Lee', 'Fiction', 'A novel about racial injustice...'),
    ('1984', 'George Orwell', 'Dystopian', 'A novel about a totalitarian regime...')
''')

cursor.execute('''
    INSERT INTO reviews (user_id, book_id, rating, comment) VALUES
    (1, 1, 5, 'A masterpiece!'),
    (1, 2, 4, 'Very moving.'),
    (2, 3, 5, 'A chilling prediction of the future.')
''')

cursor.execute('''
    INSERT INTO favorites (user_id, book_id) VALUES
    (1, 1),
    (2, 3)
''')

# Commit changes and close connection
conn.commit()
conn.close()

print('Database populated successfully.')
