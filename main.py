def main():
    report("books/frankenstein.txt")
    

def word_counter(text: str) -> int:
    return len(text.split())

def letters_counter(text: str) -> dict:
    d = {}
    for c in text.lower():
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d


def sort_on(dict):
    return dict["num"]

def report(filename: str):
    with open(filename) as f:
        text = f.read()

        words_count = word_counter(text)
        letters = letters_counter(text)

        list_chars = []
        for l in letters:
            if l.isalpha():
                list_chars.append({"letter": l, "num": letters[l]})

        list_chars.sort(reverse=True, key=sort_on)
        
        print(f"--- Begin report of {filename} ---")
        print(f"{words_count} words found in the document")

        for c in list_chars:
            char, num = c["letter"], c["num"]
            print(f"The {char} character was found {num} times")

        print("--- End report ---")

main()