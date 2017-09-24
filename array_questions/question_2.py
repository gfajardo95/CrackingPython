def map_chars_to_occurrence(str):
    string_map = {}

    for char in str:
        if char in string_map:
            string_map[char] += 1
        else:
            string_map[char] = 1

    return string_map


def is_perm_v1(str1, str2):
    if len(str1) < len(str2):
        return False
    else:
        # map the chars to their count
        char_count = map_chars_to_occurrence(str1)

    for char in str2:
        if char in char_count:
            char_count[char] -= 1
            if char_count[char] < 0:
                return False
        else:
            return False

    return True


# improve space complexity by dropping the dictionary, but becomes O(log N)
def is_perm_v2(str1, str2):
    if len(str1) < len(str2):
        return False
    else:
        sorted1 = sorted(str1)
        sorted2 = sorted(str2)

    i = 0
    j = 0
    while i < len(sorted2):
        if j is len(sorted1):
            return False
        current_char = sorted2[i]
        while j < len(sorted1):
            if sorted1[j] is current_char:
                j += 1
                i += 1
                break
            else:
                j += 1

    return True


def main():
    print(is_perm_v1('hello', 'asdfa'))
    print(is_perm_v2('hello', 'olle'))


if __name__ == '__main__':
    main()