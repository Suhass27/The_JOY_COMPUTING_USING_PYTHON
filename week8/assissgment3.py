# L = list(map(int, input().split()))
for i in L:
  if i==0:
    L.remove(i)
    L.append(i)
print(L,end="")