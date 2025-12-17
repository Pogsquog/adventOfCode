import copy

from shared import load_data1, load_data3
from typing import List


def count_neighbours(dataset, y, x, y_size, x_size):
    y_min = 0 if y == 0 else y - 1
    x_min = 0 if x == 0 else x - 1
    y_max = y if y + 1 == y_size else y + 1
    x_max = x if x + 1 == x_size else x + 1

    total = 0
    for row in dataset[y_min:y_max + 1]:
        for column in row[x_min:x_max + 1]:
            if column == '@':
                total += 1

    return total - 1  # subtract one for this square

def day4_aux(dataset):
    y_size = len(dataset)
    x_size = len(dataset[0])

    num_removable = 0
    for y in range(0, y_size):
        for x in range(0, x_size):
            if dataset[y][x] == '@' and count_neighbours(dataset, y, x, y_size, x_size) < 4:
                num_removable += 1
    print(num_removable)

def day4_aux2(dataset):
    dataset_new = copy.deepcopy(dataset)

    y_size = len(dataset)
    x_size = len(dataset[0])

    num_removable = 0
    for y in range(0, y_size):
        for x in range(0, x_size):
            if dataset[y][x] == '@' and count_neighbours(dataset, y, x, y_size, x_size) < 4:
                num_removable += 1
                dataset_new[y][x] = '.'

    return num_removable + day4_aux2(dataset_new) if num_removable > 0 else 0


def day4():
    dataset = load_data3('data/day4')
    print(day4_aux2(dataset))
