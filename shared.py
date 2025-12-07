def load_data1(filename):
    return open(filename).read().splitlines()

def load_data2(filename):
    # input is lke: 1-3,5-7,...
    data = open(filename).read().split(',')
    return [x.split('-') for x in data]
