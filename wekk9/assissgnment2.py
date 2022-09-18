def mergeDic(d1,d2):
    for k in d2:
        if k not in d1:
            d1[k] = d2[k]
    return d1

# key = list(map(int, input().split()))
# val = list(map(int, input().split()))

# d1 = {}
# for i in range(len(key)):
#     d1[key[i]] = val[i]
    
# d2 = {}
# key = list(map(int, input().split()))
# val = list(map(int, input().split()))
# for i in range(len(key)):
#     d2[key[i]] = val[i]

# print(mergeDic(d1, d2))