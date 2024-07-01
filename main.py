from fastapi import FastAPI
from assign import fetch_top_books, get_top_ten_books, select_one_book

app = FastAPI()

@app.get("/books/{genre}")
async def get_books(genre: str):
    books = fetch_top_books(genre)
    top_ten_books = get_top_ten_books(books)
    return {"top_ten_books": top_ten_books}

@app.post("/books/select")
async def select_book(genre: str, preference: str):
    books = fetch_top_books(genre)
    top_ten_books = get_top_ten_books(books)
    selected_book = select_one_book(top_ten_books, preference)
    return {"selected_book": selected_book}

@app.get("/conclude")
async def conclude():
    return {"message": "Thank you for using the book recommendation agent!"}

if __name__ == "__main__":
    import uvicorn
   