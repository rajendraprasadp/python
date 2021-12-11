def bsp(S, T):
    s = []
    for i in S:
        if i == '#':
            s.pop()
        else:
            s.append(i)

    t = []
    for j in T:
        if j == '#':
            t.pop()
        else:
            t.append(j)

    if ''.join(s) == ''.join(t):
        return True
    else:
        return False


x = bsp("acb#v#v#bc#", "acb")
print(x)
