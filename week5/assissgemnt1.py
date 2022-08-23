'''You are given a string S. Write a function count_letters which accepts the string S and returns a dictionary containing letters 
(including special character) in string S as keys and their count in string S as values.'''

dict = {}
def count_letters(s):
    for i in range(len(s)):
        dict[s[i]] = s.count(s[i])
    return dict
# s = "The Joy of computing"
# print(count_letters(s))