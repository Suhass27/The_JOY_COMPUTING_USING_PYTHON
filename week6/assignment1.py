def get_index(l,i):
    indices= []
    for idx,value in enumerate(l):
        if value==i:
            indices.append(idx)
    return indices

l = [int(i) for i in input().split()]
dict = {}
for i in l:
    ans = get_index(l,i) 
    if len(ans)>=2 :
        dict[i] = ans
print(dict)