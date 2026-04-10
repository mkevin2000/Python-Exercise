def combine(*args):
    """combine multiple lists into one list"""
    total=0
    for value in args:
        total+=value
    return total
L1=[1,2,3]
L2=[4,5,6]
L3=[7,8,9]
combine(L1,L2,L3)
print(combine(L1,L2,L3))