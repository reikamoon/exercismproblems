# An isogram (also known as a "nonpattern word") is a term in recreational linguistics. It has been used with two different definitions:
#
# A word or phrase without a repeating letter;[1][2][3] or
# A word or phrase where every letter appears the same number of times.[4][2][5]

def is_isogram(word):
    """Determine if a word is an isogram"""
    letters = set()

    for letter in word:
        if letter in letters and letter != '-' and letter != ' ':
            return False
        else:
            letters.add(letter)
    return True


if __name__ == '__main__':
    # Expected outputs: True, False
    good_test_cases = ["abolishment", "isograms"]

    # Expected outputs: Error, Error
    bad_test_cases = [55, None]

    # Expected outputs: True, True
    edge_cases = ["", "      "]

    print("Good test cases:")
    for case in good_test_cases:
        print(f"Testing '{case}'")
        print(is_isogram(case))

    print("\nBad test cases:")
    for case in bad_test_cases:
        print(f"Testing '{case}'")
        try:
            print(is_isogram(case))
        except TypeError:
            print("Error")

    print("\nEdge cases:")
    for case in edge_cases:
        print(f"Testing '{case}'")
        print(is_isogram(case))
