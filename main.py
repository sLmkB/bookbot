def countWords(s):
    return len(s.split())

def countLetters(s):
    letter_dict = {}
    for letter in s.lower():
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    return letter_dict

def main():
    filename = "./books/frankenstein.txt" 
    with open(filename) as f:
        text = f.read()
        # print(text, countWords(text), countLetters(text))
        word_count = countWords(text)
        letter_count_dict = countLetters(text)
        print(f"--- Begin report of {filename} ---")
        print(f"{word_count} words found in the document")
        print()
        sorted_letter_count_dict = dict(sorted(letter_count_dict.items(), key=lambda item: item[1], reverse=True))
        for k,v in sorted_letter_count_dict.items():
            if k.isalpha():
                print(f"The '{k}' character was found {v} times")
        print("--- End report ---")
main()