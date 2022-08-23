'''Write a program to take string S as an input and replace all vowels by *. Also print the modified string'''
def replace_the_word(s):
    vowel= 'AEIOUaeiou'
    for ele in vowel:
        s= s.replace(ele,'*')
    return s



s = input()
print(replace_the_word(s),end="")
