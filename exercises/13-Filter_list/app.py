allNumbers = [23,12,35,5,3,2,3,54,3,21,534,23,42,1]


def filter_function(items):
    if items > 10:
        return items 

greater_than = list(filter(filter_function, allNumbers))
print(greater_than)