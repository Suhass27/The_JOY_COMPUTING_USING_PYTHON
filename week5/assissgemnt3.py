'''You are given a list L. Write a program to print first prime number encountered in the list L.
(Treat numbers below and equal to 1 as non prime)'''
L = [1,2,3,4,5,6,7,8,9]
def solve(n,i):
  if (n==0 or n== 1):
    return False
  if(n==i):
    return True
  if(n%i==0):
    return False
  i+=1
  
  return solve(n,i)
  
  
for i in L:
  if solve(n=i,i=2):
    ans = i
    break
    
print(ans,end="")
    