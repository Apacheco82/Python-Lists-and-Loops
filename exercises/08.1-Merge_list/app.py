chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    #Your code go here:
    aux = []
    for item in list1:
        aux.append(item)
    for item in list2:
        aux.append(item)
    return aux    
    
print(merge_list(chunk_one, chunk_two))
