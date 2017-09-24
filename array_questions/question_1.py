# Learning Questions:
# how to get input from the user?
# how to analyze each string from the input?
# Interview Question: How to check if a string has unique characters? What if you can't use another data structure?

class StringChecker:
    # this is simple iteration
    # for c in str:
    #     print(c)

    # what's needed is an offset, so I like the C way
    def check_first_try(self, s):
        print('the test input is: ' + s)

        i = 0
        unique = True
        while i < len(s) and unique:
            j = i + 1
            while j < len(s) and unique:
                if s[i] is s[j]:
                    print(s[i] + ' is a duplicate char')
                    unique = False
                j += 1
            i += 1

# sorting the string is an optimization.. but the best I can do with sorting is log n
# also made sure not to check through the whole string if the next char is different
    def check_second_try(self, s):
        print('the test input is: ' + s)
        s = ''.join(sorted(s))

        i = 0
        unique = True
        while i < len(s) and unique:
            j = i + 1
            while j < len(s) and unique:
                if s[i] is s[j]:
                    print(s[i] + ' is a duplicate char')
                    unique = False
                else:
                    j += 1
                    break
            i += 1


print('first algorithm')
StringChecker.check_first_try(StringChecker, 'abcdec')
print('second algorithm')
StringChecker.check_second_try(StringChecker, 'abcdec')
