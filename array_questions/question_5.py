def get_len_stat(s1, s2):
    equal_len = False
    greater_len = False
    less_len = False
    bad_len = False
    len_difference = len(s1) - len(s2)

    if len_difference == 1:
        greater_len = True
    elif len_difference == 0:
        equal_len = True
    elif len_difference == -1:
        less_len = True
    else:
        bad_len = True

    return equal_len, greater_len, less_len, bad_len


def is_one_or_zero_edits_away(s1, s2):
    equal_len, greater_len, less_len, bad_len = get_len_stat(s1, s2)
    if bad_len:
        return False

    edited = False
    i = 0
    while i < len(s1) or i < len(s2):
        if i == len(s2):
            if edited:
                return False
            else:
                return True
        if i == len(s1):
            if edited:
                return False
            else:
                return True
        if s1[i] != s2[i]:
            if not edited:
                # NOTE: you don't actually need to edit the string, just pretend to! similar to the special cases above
                if equal_len:
                    l, r = s2[:i], s2[i+1:]
                    substrings = (l, s1[i], r)
                    s2 = "".join(substrings)
                    edited = True
                elif greater_len:
                    l, r = s2[:i], s2[i:]
                    substrings = (l, s1[i], r)
                    s2 = "".join(substrings)
                    edited = True
                elif less_len:
                    l, r = s1[:i], s1[i:]
                    substrings = (l, s2[i], r)
                    s1 = "".join(substrings)
                    edited = True
            else:
                return False
        i += 1

    return True


# improvement: all we need is to imitate an edit, not actually do one!
def is_one_edit_away(str1, str2):
    if (abs(len(str1) - len(str2)) > 1):
        return False

    if len(str1) < len(str2):
        s1 = str1 # shorter
        s2 = str2 # longer
    elif len(str1) > len(str2):
        s1 = str2
        s2 = str1
    else:
        s1 = str1
        s2 = str2

    found_difference = False
    index1 = 0
    index2 = 0
    while index1 < len(s1) and index2 < len(s2):
        if s1[index1] != s2[index2]:
            if found_difference:
                return False
            else:
                found_difference = True
                if len(s1) == len(s2):
                    index1 += 1
        else:
            index1 += 1
        index2 += 1

    return True


def main():
    string1 = "ebce"
    string2 = "bcd"
    print(get_len_stat(string1, string2))
    print(is_one_or_zero_edits_away(string1, string2))
    print(is_one_edit_away(string1, string2))


if __name__ == '__main__':
    main()