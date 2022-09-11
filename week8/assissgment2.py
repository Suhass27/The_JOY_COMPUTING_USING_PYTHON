def replaceV(s):
    a = s
    l = list("aeiou"+"AEIOU")
    for i in range (len(s)-2):
        if s[i] in l and s[i+1] in l and s[i+2] in l:
            a =  a.replace(s[i]+s[i+1]+s[i+2],'_')
    return a
             
# S = input()
# print(replaceV(S))