def load_data1(filename):
    return open(filename).read().splitlines()

def load_data2(filename):
    # input is lke: 1-3,5-7,...
    data = open(filename).read().split(',')
    return [x.split('-') for x in data]

def load_data3(filename):
    dataset = load_data1(filename)
    # turn a list of strings into a 2d array of chars
    return [list(line) for line in dataset]

def load_data4(filename):
    # input is like 1-3\n5-7\n\n3n5
    data = load_data1(filename)

    ranges = []
    ids = []

    section = 0
    for row in data:
        if row == '':
            section = 1
            continue
        else:
            if section == 0:
                ranges.append([int(x) for x in row.split('-')])
            else:
                ids.append(int(row))

    return ranges, ids
