def solve(s):
    ans=""
    for i in range(len(s)):
        letter = s[i]
        
        if letter==" ":
            ans+=" "
        elif (letter.isupper()):
            ans+=chr((ord(letter) -3 -65)%26 +65)
        elif (letter.islower()):
            ans+=chr((ord(letter)-2 -97)%26 +97)
        else :
            ans+=letter
    return ans
    
s = input()
print(solve(s),end="")