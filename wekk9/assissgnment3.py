# n = int(input())
N = list(str(n))
p = []
for i in N:
    if i not in p:
        p.append(i)
ans = []
for i in range(len(p)):
    a = []
    for j in range(len(N)):
        if(p[i]==N[j]):
            a.append(j)
    ans.append(a)

for i in range(len(p)):
    print(int(p[i]),"",end="")
    for j in range(len(ans[i])):
        print(int(ans[i][j]),"",end="")
    if(i!=len(p)-1):
        print()