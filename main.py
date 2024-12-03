def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = amount_of_words(text)
    char_count_dicts = count_characters(text)
    chars_sorted_list = chars_dict_to_sorted_list(char_count_dicts)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print()
    
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End report ---")

def amount_of_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def sort_dict(char_count_dicts):
    return char_count_dicts["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sort_list = []
    for ch in num_chars_dict:
        sort_list.append({"char": ch, "num": num_chars_dict[ch]})
    sort_list.sort(reverse=True, key=sort_dict)
    return sort_list

def get_book_text(path):
    with open(path) as file:
        return file.read()


main()