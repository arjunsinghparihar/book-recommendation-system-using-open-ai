import requests

# Define a function to fetch top books from an API
def fetch_top_books(genre, limit=100):
    # Here you can integrate with a real books API or use a mock response
    # For demonstration, we'll use a mock response
    mock_response = [{"title": f"Book {i+1}", "genre": genre} for i in range(limit)]
    return mock_response

# Define a function to get the top 10 books
def get_top_ten_books(books):
    # For demonstration, we'll assume the first 10 books are the top 10
    return books[:10]

# Define a function to select one book from the top 10
def select_one_book(top_ten_books, user_preference):
    # For simplicity, let's return the first book that matches the user preference
    for book in top_ten_books:
        if user_preference.lower() in book["title"].lower():
            return book
    return top_ten_books[0]  # Return the first book if no match is found
