import streamlit as st
import requests

st.title("Book Recommendation Agent")

genre = st.text_input("Enter a genre:")
if st.button("Find Top 100 Books"):
    response = requests.get(f"http://localhost:8000/books/{genre}")
    if response.status_code == 200:
        top_ten_books = response.json()["top_ten_books"]
        st.write("Top 10 Books in Genre:")
        for i, book in enumerate(top_ten_books):
            st.write(f"{i+1}. {book['title']}")

        preference = st.text_input("Enter your preference for a book title:")
        if st.button("Select Book"):
            select_response = requests.post("http://localhost:8000/books/select", params={"genre": genre, "preference": preference})
            if select_response.status_code == 200:
                selected_book = select_response.json()["selected_book"]
                st.write(f"Selected Book: {selected_book['title']}")
                conclude_response = requests.get("http://localhost:8000/conclude")
                st.write(conclude_response.json()["message"])
else:
    st.write("Enter a genre to start the recommendation process.")
