'''Write a function rev which takes a list L and integer n and print the first n largest numbers of the list'''
s = []
def rev(l,n):
  l.sort()
  l.reverse()
  for i in range(n):
    s.append(l[i])
  print(s,end="")

