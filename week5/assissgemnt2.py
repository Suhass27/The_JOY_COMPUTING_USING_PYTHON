'''You are given a list L. Write a function uniqueE which will return a list of unique elements is the 
list L in sorted order. (Unique element means it should appear in list L only once.)'''
ans =[]
#dict={}
def uniqueE(l):
  for i in l:
    if(l.count(i)==1):
      ans.append(i)
  ans.sort()
  return (ans)