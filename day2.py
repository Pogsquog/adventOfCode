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

def day2_aux2(dataset):
    result = 0
    for item in dataset:
        for x in range(int(item[0]), int(item[1])+1):
            y = str(x)
            strlen = len(y)
            for i in range(2, strlen + 1):
                if strlen % i != 0: # can't split in this many
                    continue
                if y[0:strlen//i]*i == y:
                    if i != 2:
                        print(y)
                    result += x
                    break
    print(result)

def day2():
    dataset = load_data2('data/day2')
    day2_aux2(dataset)
