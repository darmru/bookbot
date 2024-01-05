def main():
    book_path = "books/frankenstein.txt"
    print(f"--- Begin raport of {book_path} ---")
    text = get_book_text(book_path)
    get_raport(text)
    print("--- End raport ---")


def get_raport(text):
    
    print(f"{get_num_words(text)} words found in the document")
    print('')
    raportList = list(get_num_characters(text).items())
    raportList.sort()
    for item in raportList:
        if item[0].isalpha():
            print(f"The '{item[0]}' character was found {item[1]} times")



def get_num_characters(text):
    characters = {}
    words = ''.join(text.split())
    words = words.lower()
    for char in words:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()