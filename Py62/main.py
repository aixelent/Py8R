import itertools

chars = ['a', 's', 'x', 'j']
c = 4

while c > 0:
    s = list(itertools.permutations(chars, c))
    print(["".join(i) for i in s])
    c -= 1
