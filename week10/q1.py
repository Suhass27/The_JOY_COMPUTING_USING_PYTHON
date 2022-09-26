L = [int(i) for i in input().split()]
L.sort()
l = max(L)
ans =[]
for i in range(0,l+1):
    if i in L:
        print(i,end=" ")
    else:
        print(0,end=" ")
