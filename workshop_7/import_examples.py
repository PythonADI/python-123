import math
import datetime as dt
from collections import Counter
from random import randint as random_int


def circle_area(radius):
    return math.pi * radius ** 2


def most_common(items):
    counter = Counter(items)
    return counter.most_common(1)[0]


def utc_timestamp():
    return dt.datetime.now()


if __name__ == "__main__":
    print("circle area", circle_area(3))
    print("random int", random_int(1, 10))
    print("most common", most_common(["apple", "apple", "pear", "banana"]))
    print("timestamp", utc_timestamp())
