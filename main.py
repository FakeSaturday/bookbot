def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = amount_of_words(text)
    print(f"Amount of words in book: {word_count}")

def amount_of_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()