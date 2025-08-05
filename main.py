from stats import count_words, character_count, sorted_dict
import sys

def get_book_details(filePath: str) -> str:

    with open(filePath) as f:
        fileContents: str = f.read()

    return fileContents



def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    bookPath = sys.argv[1]
    book: str = get_book_details(bookPath)
    # print(book)
    wordCount: int = count_words(book)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookPath}")
    print("----------- Word Count ----------")
    print(f"Found {wordCount} total words")
    print("--------- Character Count -------")

    characterCount: dict = character_count(book)
    sortedCharacters: list = sorted_dict(characterCount)

    for item in sortedCharacters:
        print(f"{item["char"]}: {item["num"]}")



    print("============= END ===============")


main()
