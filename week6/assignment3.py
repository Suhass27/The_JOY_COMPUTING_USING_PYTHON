def solve(s):
    if len(s)==0:
        return True
    return s==s[::-1]

s = input().lower()
if (solve(s)):
    print("palindrome",end="")
else:
    print("not palindrome",end="")