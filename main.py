def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    dict = get_num_letters(text)
    dict_list = get_dict_to_list(dict)
    
    print(f"{num_words} words found in the document")

    for l in dict_list:
        print(f"The '{l[0]}' character was found {l[1]} times")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_letters(text):
    dictLetters = {}
    for letter in text:
        letter_lowered = letter.lower()
        if(letter_lowered in dictLetters):
            dictLetters[letter_lowered] += 1
        else:
            dictLetters[letter_lowered] = 1
    
    return dictLetters

def get_dict_to_list(char_list):
    dictList = []

    for key, value in char_list.items():
        if(key.isalpha()):
            dictList.append([key, value])

    dictList = sorted(dictList, key=lambda d: d[1], reverse=True)

    return dictList

main()