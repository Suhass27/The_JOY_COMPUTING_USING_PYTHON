a = int(input())
b = int(input())
l = []
for i in range(a,b+1):
    if(i==1):
        continue
    for j in range(2,i//2+1):
        if(i%j==0):
           l.append(i)
           break
#t = set(l)
for i in range(len(l)):
    if(i!=len(l)-1):
        print(l[i])
    else:
        print(l[i],end="")

    