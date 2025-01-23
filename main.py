def main():
    text = "books/frankenstein.txt"
    book_text = get_book_text(text)
    count_of_chars = count_chars(book_text)
    num_of_chars = amount_of_chars(book_text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_of_chars} words found in the document")
    print()
    print(num_of_chars)
    print("--- End report ---")

def get_book_text(text):
    with open(text) as f:
        return f.read()
    
def count_chars(book_text):
    words = len(book_text.split())
    return words

def amount_of_chars(book_text):
    text_dict = {}
    book_text = book_text.lower()
    for character in book_text:
        if character not in text_dict:
            text_dict[character] = 1
        else:
            text_dict[character] += 1

    return text_dict

def sorted_dict(text_dict):
    return text_dict["character"]





main()