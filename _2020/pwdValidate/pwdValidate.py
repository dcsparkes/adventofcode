def charLimit(min: int, max: int, char, string):
    """Ensure that the count of occurrences of char in string lies between min and max"""

    if max < min:
        raise(ValueError('max less than min.'))

    total = string.count(char)
    return total <= max and total >= min


def parityOddCount(a: int, b: int, char, string):
    """Ensure that the count of occurrences of char in string in positions a & b is exactly 1"""
    return (string[a-1] == char) ^ (string[b-1] == char)


def checkPwdParams(line, func=charLimit):
    """Extract parameters from string and use *func to pwdValidate password."""
    parts = line.split(' ')

    a, b = parts[0].split('-')
    char = parts[1].strip(':')
    return func(int(a), int(b), char, parts[2])


def checkFile(fileName, func=charLimit):
    count = 0
    with open(fileName) as inFile:
        for line in inFile:
            if(checkPwdParams(line, func)):
                count += 1
    return count

