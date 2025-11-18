def calculate_average(*nums):
    print(nums, type(nums))
    s = 0

    for num in nums:
        s += num

    return s / len(nums)


def greet(user, user2, user3, *names):
    print(f"Hello {user}")
    print(f"Hello {user2}")
    print(f"Hello {user3}")

    for u in names:
        print(f"Hello {u}")


print(calculate_average(4, 4, 5, 5, 5, 6, 7, 1, 3))


greet("Nika", "George", "Gela", "GiGi", "Marry")