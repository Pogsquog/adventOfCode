from shared import load_data1
from typing import List


def battery_sum(battery: List[int], num_digits):
    # make the biggest num_digit number using the numbers in battery
    search_length = len(battery) - num_digits + 1

    # find the highest number's index in 0-search_length of the digits
    leading_digits = battery[:search_length]
    highest_index = leading_digits.index(max(leading_digits))
    highest_value = leading_digits[highest_index]

    rest_of_values = battery_sum(battery[highest_index + 1:], num_digits-1) if num_digits > 1 else 0
    return 10**(num_digits - 1) * highest_value + rest_of_values

assert(battery_sum([1], 1) == 1)
assert(battery_sum([1,2], 2) == 12)
assert(battery_sum([1,2,3], 2) == 23)
assert(battery_sum([3,1,2], 2) == 32)
assert(battery_sum([9,8,7,6,5,4,3,2,1,1,1,1,1,1,1], 12) == 987654321111)
assert(battery_sum([8,1,1,1,1,1,1,1,1,1,1,1,1,1,9], 12) == 811111111119)
assert(battery_sum([2,3,4,2,3,4,2,3,4,2,3,4,2,7,8], 12) == 434234234278)
assert(battery_sum([8,1,8,1,8,1,9,1,1,1,1,2,1,1,1], 12) == 888911112111)



def day3_aux2(dataset):
    total = 0
    for battery in dataset:
        result = battery_sum([int(x) for x in battery], 12)
        # print(result)
        total += result
    print(total)

def day3_aux(dataset):
    result = 0
    for battery in dataset:
        # find the highest first digit
        high1 = -1
        high1_index = 0
        for i in range(len(battery)-1):
            if int(battery[i]) > high1:
                high1 = int(battery[i])
                high1_index = i
        high2 = -1
        high2_index = 0

        # find the highest second digit after the highest first digit
        for i in range(high1_index+1, len(battery)):
            if int(battery[i]) > high2:
                high2 = int(battery[i])
                high2_index = i

        jolts = high1 * 10 + high2
        print(jolts, high1_index, high2)
        result += jolts

    print(result)


def day3():
    dataset = load_data1('data/day3')
    # day3_aux(dataset)
    day3_aux2(dataset)
