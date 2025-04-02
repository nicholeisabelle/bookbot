import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read() 
    return file_contents

from stats import get_num_words
from stats import get_num_char 
from stats import get_sorted_list

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    word_count = get_num_words(book_text)
    char_count = get_num_char(book_text)
    sorted_list = get_sorted_list(char_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for pair in sorted_list:
        char = pair["character"]
        count = pair["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

main()



