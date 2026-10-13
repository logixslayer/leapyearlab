import sys

def isLeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    year = int(sys.argv[1])

    if isLeapYear(year):
        print(year, "is a Leap Year")
    else:
        print(year, "is not a Leap Year")