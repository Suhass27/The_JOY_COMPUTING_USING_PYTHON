def cubeT(l):
    ans = []
    for i in l:
        ans.append(i*i*i)
    return tuple(ans)
# L = [int(i) for i in input().split()]
# print(cubeT(L))