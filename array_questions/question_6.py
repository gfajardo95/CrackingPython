# String compression
def map_char_to_count(s1):
    char_to_count_map = {}
    char_count = 0
    good_compression = True

    for char in s1:
        if char in char_to_count_map:
            char_to_count_map[char] += 1
        else:
            char_to_count_map[char] = 1

    return char_to_count_map


def compress_string(s1):
    char_count= map_char_to_count(s1)
    compressed_length = len(char_count) * 2

    if compressed_length >= len(s1):
        return s1
    compressed = []

    for char in char_count:
        compressed.append(char + str(char_count[char]))

    return ''.join(compressed)


def main():
    test1 = "abcdefg"
    test2 = "aa"
    test3 = "aaa"
    test4 = "aaab"
    test5 = "aaabb"

    print("{0}. compressed string is: {1}".format(test1, compress_string(test1)))
    print("{0}. compressed string is: {1}".format(test2, compress_string(test2)))
    print("{0}. compressed string is: {1}".format(test3, compress_string(test3)))
    print("{0}. compressed string is: {1}".format(test4, compress_string(test4)))
    print("{0}. compressed string is: {1}".format(test5, compress_string(test5)))


if __name__ == '__main__':
    main()