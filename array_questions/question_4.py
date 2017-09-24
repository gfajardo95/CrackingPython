def map_chars_to_occurrence(str):
    string_map = {}

    for char in str:
        if char in string_map:
            string_map[char] += 1
        elif char != " ":
            string_map[char] = 1

    return string_map


def is_odd(number):
    if number % 2:
        return True
    else:
        return False


def is_palindrome(my_str):
    char_count = map_chars_to_occurrence(my_str)
    odd_len = False
    odd_count = 0

    substrings = my_str.split(sep=" ")
    str_without_spaces = "".join(substrings)

    if is_odd(len(str_without_spaces)):
        odd_len = True

    for key in char_count:
        if is_odd(char_count[key]):
            if odd_count < 1 and odd_len:
                odd_count += 1
            else:
                return False

    return True


def main():
    test_input = "tact coa"
    print(is_palindrome(test_input))


if __name__ == '__main__':
    main()