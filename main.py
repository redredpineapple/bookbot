from stats import get_num_words
from stats import get_word_freq
from stats import sort_dict
import sys

def get_book_text(file):
    with open(file) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    

    content = get_book_text(path)
    num_words = get_num_words(content)
    word_freq = get_word_freq(content)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    sorted_word_freq = sort_dict(word_freq)

    for i in sorted_word_freq:
        if i.isalpha():
            print(f"{i}: {sorted_word_freq[i]}")
    


main()
