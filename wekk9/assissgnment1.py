def subStr(s1,s2):
    #return (s2 in s1)
    n1,n2 = len(s1),len(s2)
    if(n2>n1):
        return False
    for i in range(n1-n2+1):
        s = s1[i:i+n2]
        if s==s2:
            return True
    return False
            
    
# s1 = input()
# s2 = input()
# print(subStr(s1,s2))