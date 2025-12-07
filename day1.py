from shared import load_data1


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

def day1_aux2(dataset):
    num_zeroes = 0
    current_position = 50

    # print(f"{current_position}, {num_zeroes}")

    for item in dataset:
        # convert format like l3 = -3, r7 = 7
        item_lr = item[0]
        item_num = int(item[1:])
        if item_lr == 'L':
            item_num *= -1

        previous_position = current_position
        current_position += item_num
        wrapped_left = current_position<0

        while True:
            if current_position < 0:
                current_position += 100
                num_zeroes += 1
            elif current_position >= 100:
                current_position -= 100
                if current_position != 0:
                    num_zeroes += 1
            elif current_position == 0:
                num_zeroes += 1
                break
            else:
                break

        if previous_position == 0 and wrapped_left:
            num_zeroes -= 1

        # print(f"{item}, {current_position}, {num_zeroes}")

    print(num_zeroes)

def day1():
    dataset = load_data1('data/day1')
    day1_aux(dataset)
    day1_aux2(dataset)