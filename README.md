# Project Name: BookHub - Book Recommendation System

## Project Description

BookHub is a web application built with Python and Flask that provides personalized book recommendations based on user preferences. Users can explore new books, read reviews, and mark their favorites.

### Features

- **User Registration and Authentication:** Users can sign up, log in, and manage their profiles.
- **Book Recommendations:** Recommends books based on genres, user ratings, and similar user preferences.
- **Book Search:** Allows users to search for specific books by title, author, or genre.
- **Book Details:** Provides detailed information about each book, including reviews and ratings.
- **Favorite Books:** Users can mark books as favorites and create personalized reading lists.

### Technologies Used

- **Python**
- **Flask:** Micro web framework for Python.
- **SQLAlchemy:** ORM (Object Relational Mapping) library for database management.
- **HTML/CSS:** Frontend design and structure.
- **Bootstrap:** Frontend framework for responsive design.
- **SQLite:** Lightweight SQL database for storing user data and book information.

### Project Structure

- **`app.py`:** Contains the main Flask application code and routes.
- **`models.py`:** Defines SQLAlchemy models for User, Book, and Favorite relationships.
- **`templates/`:** Directory containing HTML templates for the web pages.
  - **`index.html`:** Homepage displaying recommended books and search options.
  - **`book_details.html`:** Page displaying detailed information about a specific book.
- **`static/`:** Directory containing static assets like CSS files and images.

### Contributing

Contributions are welcome! Please fork the repository and create a pull request with your proposed changes.

### License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.
