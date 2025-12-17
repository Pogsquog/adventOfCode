from shared import load_data4


def num_in(i, ranges):
    for num_range in ranges:
        if num_range[0] < i <= num_range[1]:
            return True
    return False


def day5_aux(ranges, ids):
    count = 0
    for i in ids:
        if num_in(i, ranges):
            count += 1

    print(count)


def day5():
    ranges, ids = load_data4('data/day5')
    day5_aux(ranges, ids)
