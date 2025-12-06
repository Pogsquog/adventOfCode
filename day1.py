from shared import load_data


def day1_aux(dataset):
    num_zeroes = 0
    current_position = 50

    for item in dataset:
        # convert format like l3 = -3, r7 = 7
        item_lr = item[0]
        item_num = int(item[1:])
        if item_lr == 'L':
            item_num *= -1
        current_position += item_num
        current_position = current_position % 100
        if current_position == 0:
            num_zeroes += 1

    print(num_zeroes)

def day1():
    dataset = load_data('data/day1')
    day1_aux(dataset)