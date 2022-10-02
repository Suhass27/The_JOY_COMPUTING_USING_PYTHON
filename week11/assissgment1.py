a = int(input())
b = int(input())
c = int(input())
if(((a**2+ b**2)==c**2) or ((a**2 + c**2)==b**2) or ((b**2+c**2)==a**2)):
    print("YES",end="")
else:
    print("NO",end="")