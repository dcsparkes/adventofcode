def validateQuick(record):
    essentialKeys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    for key in essentialKeys:
        if key not in record:
            return False
    return True

def ValidateThorough(record):
    # essentialKeys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    if validateQuick(record) and \
        isYearinRange(record["byr"], 1920, 2002) and \
        isYearinRange(record["iyr"], 2010, 2020) and \
        isYearinRange(record["eyr"], 2020, 2030) and \
        isValidHeight(record["hgt"]) and \
        isValidHair(record["hcl"]) and \
        isValidEye(record["ecl"]) and \
        isValidPID(record["pid"]):
        # print(record["byr"], record["iyr"], record["eyr"], record["hcl"], record["ecl"], record["pid"])

        return True

def isValidEye(colour):
    return colour in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def isValidHair(colour):
    retVal = False
    if len(colour) == len("#000000") and colour[0] == '#':
        retVal = True
        for c in colour[1:]:
            retVal &= c in "1234567890abcdef"

    return retVal

def isValidHeight(height):
    units = height[-2:]

    if height[:-2].isdigit():
        value = int(height[:-2])
        if units == "cm":
            return value >= 150 and value <= 193

        elif units == "in":
            return value >= 59 and value <= 76

    return False

def isValidPID(id):
    return len(id) == 9 and id.isdigit()

def isYearinRange(year, lower=1000, upper=9999):
    # print(year)
    # print("{}:{}:{}".format(year, len(year), int(year)))

    lengthCorrect = len(year) == 4
    year = int(year)
    lower = int(lower)
    upper = int(upper)

    if upper < lower:
        raise(ValueError('upper less than lower.'))

    if lower < 1000:
        raise(ValueError('4 digit years only.'))

    return lengthCorrect and year >= lower and year <= upper

def validCount(fileName, validate=validateQuick):
    record = dict()
    count = 0

    with open(fileName) as inFile:
        for line in inFile:
            fields = line.split()
            if len(fields):
               for field in fields:
                   key, value = field.split(':')
                   record[key] = value

            else:
                if validate(record):
                    count += 1
                record = dict()

    # Catch last record
    if record and validate(record):
        count += 1

    return count
