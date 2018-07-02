"""
Find the median of two unsorted arrays
"""


def median_two_arrays(first, second):
    temp = first + second
    final = sorted(temp)

    middle = len(final) // 2

    if len(final) % 2 != 0:
        print(final[middle])
    else:
        avg = (final[middle] + final[middle - 1]) / 2
        print(avg)


first_list = [1, 2]
second_list = [3, 2, 7, 6]

median_two_arrays(first_list, second_list)
