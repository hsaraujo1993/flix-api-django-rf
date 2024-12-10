# Movie Review API

This project is a Django Rest Framework (DRF) application designed for managing movies, genres, actors, and user reviews. It allows users to interact with these entities through RESTful APIs.

## Features

- **Movies**: Manage movie details including title, release year, and related genres and actors.
- **Genres**: Add and list genres associated with movies.
- **Actors**: Add and list actors linked to movies.
- **Reviews**: Users can add reviews to movies.

## Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:hsaraujo1993/moviereview-api.git
   cd moviereview-api
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Project Structure

- **actors/**: Manages actor-related data.
- **app/**: Core Django application logic.
- **genres/**: Handles genre-related operations.
- **movies/**: Contains logic for managing movies.
- **reviews/**: Manages user reviews.

## API Endpoints

### Movies
- `GET /movies/`: List all movies.
- `POST /movies/`: Create a new movie.

### Genres
- `GET /genres/`: List all genres.
- `POST /genres/`: Add a new genre.

### Actors
- `GET /actors/`: List all actors.
- `POST /actors/`: Add a new actor.

### Reviews
- `GET /reviews/`: List all reviews.
- `POST /reviews/`: Add a review for a movie.
