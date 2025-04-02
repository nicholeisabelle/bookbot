def get_num_words(book):
    words = book.split()
    word_count = len(words)
    return word_count

from collections import defaultdict

def get_num_char(book):
    lower_case = book.lower()
    char_num_count = defaultdict(int)
    for char in lower_case:
        char_num_count[char] += 1
    return dict(char_num_count)

def get_sorted_list(dict):
    sorted_list = sorted(dict.items(), key=lambda item : item[1], reverse=True)
    sorted_dicts = []
    for char, count in sorted_list:
        full_dict = {"character":char, "count": count}
        sorted_dicts.append(full_dict)
    return sorted_dicts


