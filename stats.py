def count_words(book: str) -> int:
    words: int = book.split()
    return len(words)

def character_count(text: str) -> dict:
    characters: dict = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'o': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'x': 0,
    }

    for i in text:
        letter = i.lower()
        if letter in characters:
            characters[letter] += 1

    return characters

def sort_on(items):
    return items["num"]

def sorted_dict(characters: dict) -> list:
    new_list: list = []

    for k, v in characters.items():
        new_list.append({"char": k, "num": v})

    new_list.sort(reverse=True, key=sort_on)

    return new_list