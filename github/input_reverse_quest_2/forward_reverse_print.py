result =[]
def forwardprint(arg):
    for _ in range(len(arg)):
        result=list(arg)
    print(''.join(result))

def reverseprint(arg):
    for _ in range(len(arg)):
        result.append(arg.pop())
    print(''.join(result))


