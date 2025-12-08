from shared import load_data1

# highest values from an ordered list

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
    day3_aux(dataset)
