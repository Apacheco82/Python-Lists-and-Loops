names = ['Esmeralda','Kiko','Ruth','Lebron','Pedro','Maria','Lou','Fernando','Cesco','Bart','Annie']

#Your code here:
names[1] = "Steven"
names[-1] = "Pepe"

names[0] = names[2]+names[4]

"""for item in reversed(names):  mejor solución pero no pasa test
    print(item)
"""
for i in range(len(names) - 1, -1 , -1):
    print(names[i])