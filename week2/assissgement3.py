#Take a string S and an integer A as an input from a user. Write a program to print string S, A number of times.
s = input()
n =  int(input())

for i in range(n):
  if i==n-1:
    print(s,end="")
  else:
  	print(s)