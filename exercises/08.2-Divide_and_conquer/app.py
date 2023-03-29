list_of_numbers = [4,	80,	85,	59,	37, 25, 5, 64, 66, 81, 20, 64, 41, 22, 76, 76, 55, 96, 2, 68]


#Your code here:
def merge_two_list(arr1):
    odd = []
    even = []
    for item in arr1:
        if item % 2 != 0:
            odd.append(item)
        else:
            even.append(item)
    aux = []
    aux2 = []
    for item in odd:
        aux.append(item)
    for item in even:
        aux2.append(item)
    return [aux , aux2]

print(merge_two_list(list_of_numbers))

