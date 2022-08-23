'''
write program to take an integer n as an input and display the pattern
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*'''
rows = int(input())
for i in range(0, rows):
    for j in range(0, i + 1):
        print("* ", end='')
    print("")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("* ", end="")
    if j!=0:
      print("")
