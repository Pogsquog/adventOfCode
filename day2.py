from shared import load_data2

def day2_aux(dataset):
    result = 0
    for item in dataset:
        for x in range(int(item[0]), int(item[1])+1):
            y = str(x)
            strlen = len(y)
            if strlen % 2 != 0: # can't split in half
                continue
            if y[0:strlen//2] == y[strlen//2:]:
                print(y)
                result += x
    print(result)

def day2():
    dataset = load_data2('data/day2')
    day2_aux(dataset)

