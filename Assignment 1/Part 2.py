def isStringPermutation(s1: str, s2: str) -> bool:
    #immediate checks
    if (len(s1) != len(s2)):
        return False
    if (s1 ==  '') or (s2 == ''):
        return False

    letters_used = {}
    for letter in s1:
        if letter in letters_used:
            letters_used[letter] += 1
        else:
            letters_used[letter] = 1

    for letter in s2:
        if letter not in letters_used.keys():
            return False;
        letters_used[letter] -= 1
        if letters_used[letter] == 0:
            del letters_used[letter]

    return True;

def pairsThatEqualSum(inputArray: list, targetSum: int) -> list:
    result = []

    for number in inputArray:
        if (targetSum - number) in inputArray:
            if [targetSum - number, number] not in result:
                result.append([number, targetSum - number])
    print(result)


def main():
    print(isStringPermutation("asdd", "asdf"))
    print(isStringPermutation("asdf", "adf"))
    print(isStringPermutation("asdf", "df"))
    print(isStringPermutation("asdf", "fdsa"))

    pairsThatEqualSum([1, 2, 3, 4, 5], 5)
    pairsThatEqualSum([1, 2, 3, 4, 5], 1)
    pairsThatEqualSum([1, 2, 3, 4, 5], 7)


if __name__ == '__main__':
    main()