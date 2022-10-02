a = int(input())
b = int(input())
flag=0
l = []
for i in range(a,b+1):
    if(i==1):
        continue
    flag=1
    for j in range(2,i//2+1):
        if(i%j==0):
           l.append(i)
t = set(l)
for i in t:
    print(i)

    