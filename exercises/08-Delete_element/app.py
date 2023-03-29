people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name, my_list):
    #Your code go here:
    aux = []
    for i in my_list:
        if i != person_name:
            aux.append(i)
      
    return aux

    
print(deletePerson("daniella", people))
print(deletePerson("juan", people))
print(deletePerson("emilio", people))