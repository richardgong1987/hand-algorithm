def getIndex(letter: str):
    return ord(letter) - 96


def value(letter: str, power: int):
    return (2 ** power) * getIndex(letter)


def rabin_hash(sum, start, first, k):
    return (sum - value(start, k - 1)) * 2 + value(first, 0)


def find_matches(string: str, pattern: str):
    result = []
    k = len(pattern)

    pattern_hash = 0
    for i, char in enumerate(pattern):
        pattern_hash += value(char, k - i - 1)

    string_hash = 0
    for i, char in enumerate(string[:k]):
        string_hash += value(char, k - i - 1)

    if pattern_hash == string_hash:
        if string[:k] == pattern:
            result.append(0)

    for i in range(len(string) - k):
        string_hash = rabin_hash(string_hash, string[i], string[i + k], k)

        if pattern_hash == string_hash:
            if string[i + 1:i + k + 1] == pattern:
                result.append(i + 1)

    return result


print(find_matches('abcacbabc', 'abc'))
