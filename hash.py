from random import randint


def getRandom(array, digits):
    randNum = ""
    for i in range(digits):
        randNum += array[randint(0, len(array) - 1)]
    return int("%08d" % (int(randNum),))


def getMax(dict):
    size = 0

    for key in dict:
        if len(dict[key]) > size:
            size = len(dict[key])

    return size


def main(n, m):
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    dict = {}

    for i in range(m):
        dict[i] = []

    for i in range(n):
        random = getRandom(numbers, 8)
        dict[random % m].append(random)
    return getMax(dict)


if __name__ == '__main__':
    for i in range(10):
        print(main(60, 30), end=" ")
    print("\n")
    for i in range(10):
        print(main(60, 1000), end=" ")
    print("\n")
    for i in range(10):
        print(main(60, 4), end=" ")