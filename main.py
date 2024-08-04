def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    counted_characters = count_characters(text)
    counted_characters_list = chars_dict_to_sorted_list(counted_characters)
    print(f"{num_words} words found in the document")
    for item in counted_characters_list:
        if not item["char"].isalpha():
            continue
        print(f"the '{item['char']}' character was found {item['num']} times")


def count_characters(text):
    chars = {}
    text = text.lower()
    for char in text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def chars_dict_to_sorted_list (num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char":ch, "num":num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

        
def sort_on(d):
    return d["num"]

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open (path) as f:
        return f.read()

main()