def urlify_string_v1(str, true_len):
    URL_STR = "%20"
    spaces = (len(str) - true_len) / 2  # this returns a double!
    i = 0
    urlified_string = ""

    while i < len(str) and spaces != 0:
        if str[i] is " ":
            # str.insert(i, URL_STR) ERROR: str.insert does not work because insert is for lists, not strings
            bef, _, aft = str.partition(" ")
            substrings = (bef, URL_STR, aft)
            str = "".join(substrings)
            i += 3
            spaces -= 1
        else:
            i += 1
    urlified_string = str

    return urlified_string


def urlify_string_v2(str):
    URL_STR = "%20"
    urlified_string = str.rstrip(" ")  # strips trailing spaces, not necessary but good to know
    substrings = urlified_string.split(sep=" ")
    urlified_string = URL_STR.join(substrings)

    return urlified_string


def main():
    test_input = "t ab d    "
    new_str = urlify_string_v1(test_input, 6)
    print(new_str)

    test_input = "ar bcc tdd    "
    new_str = urlify_string_v2(test_input)
    print(new_str)


if __name__ == '__main__':
    main()
