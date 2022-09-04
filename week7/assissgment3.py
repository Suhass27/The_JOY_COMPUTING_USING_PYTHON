def snake(m):
    s = []
    for i in range(len(m)):
        if i%2==0:
            s+=m[i]
        else:
            s+=m[i][::-1]
    return s
# n = int(input())
# M = []
# for i in range(n):
#     L = list(map(int, input().split()))
#     M.append(L)

# print(snake(M))