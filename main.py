from stats import num_words
from stats import num_letters
from stats import character
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    word_count = num_words(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    char_counts = num_letters(book_text) # This gives you {"a": 100, "b": 50, etc.}
    sorted_chars = character(char_counts) # This gives you the sorted list of dictionaries
    for item in sorted_chars:
        char = item["char"]
        count = item["num"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

main()
