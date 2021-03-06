
def isLeapyear(n):
    '''Params: Integer N, Returns if N is a leap year based on revised Julian calendar'''
    if n % 4 == 0 and n % 100 != 0 or n % 4 == 0 and n % 900 in (200, 600):
        return True
    else:
        return False


def leaps(start, end):
    count = 0
    for i in range(start, end):
        if isLeapyear(i):
            count += 1
    return count


def main():
    print leaps(2, 1000)
    print leaps(1, 100)
    print "Expected: 1 - Actual: {}".format(leaps(2016, 2017))  # 1
    print "Expected: 0 - Actual: {}".format(leaps(2019, 2020))  # 0
    print "Expected: 0 - Actual: {}".format(leaps(1900, 1901))  # 0
    print "Expected: 1 - Actual: {}".format(leaps(2000, 2001))  # 1
    print "Expected: 0 - Actual: {}".format(leaps(2800, 2801))  # 0
    print "Expected: 1 - Actual: {}".format(leaps(123456, 123456))  # 0
    print "Expected: 1077 - Actual: {}".format(leaps(1234, 5678))  # 1077
    print "Expected: 1881475 - Actual: {}".format(leaps(123456, 7891011))  # 1881475


if __name__ == "__main__":
    main()