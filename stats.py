def num_words(book_text):
    numbers = book_text.split()
    total = len(numbers)
    return total


def num_letters(book_text):
    counts = {}
    for letter in book_text.lower():
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    return counts

def character(counts):
    char_list = []
    for char, count in counts.items():
        letters = {"char": char, "num": count}
        char_list.append(letters)
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def sort_on(dict):
    return dict["num"]
