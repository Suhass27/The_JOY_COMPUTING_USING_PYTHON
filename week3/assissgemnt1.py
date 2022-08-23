'''There is list L containing some numbers. Write a program to create a new list which contains the numbers which are either divisible by 5 or 7 or both. Print that new list in ascending order.
'''
L = [int(i) for i in input().split()]
ls = []
for i  in L :
  if i%5==0 or i%7==0 :
  	ls.append(i)
ls.sort()   
print(ls,end="")