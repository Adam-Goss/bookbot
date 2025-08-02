from stats import count_words

def get_book_details(filePath: str) -> str:

    with open(filePath) as f:
        fileContents: str = f.read()

    return fileContents



def main():
    book: str = get_book_details("./books/frankenstein.txt")
    # print(book)
    wordCount: int = count_words(book)

    print(f"{wordCount} words found in the document")

main()
