theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:
def assign(x):
    if x == 0:
        return "woko"
    else:
        return "wiki"

result = list(map(assign, theBools))
print(result)

