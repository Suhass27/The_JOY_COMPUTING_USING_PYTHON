'''Take two numbers N and K as an input. Create a list L of length N and initialize it
with zeros. Change the value to 1 of even indexes 
if k is even, otherwise change the value of odd indexes. Print list 
L in the end.(Consider 0 as even)'''
l =[]

n = int(input ())
k= int(input())
for i in range(n):
  l.append(0)
if k%2==0:
  for i in range (n):
    if i%2==0:
      l[i] = 1
else:
  for i in range (n):
    if i%2!=0:
      l[i] = 1
print(l,end="")
   