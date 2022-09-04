def DiagCalc(li):
   index = len(li)
   first_dia =  sum(li[i][i]for i in range(index))
   second_dia = sum(li[i][index-i-1]for i in range(index))
   print(first_dia)
   print(second_dia )
# n = int(input())
# M = []
# for i in range(n):
#     L = list(map(int, input().split()))
#     M.append(L)

# DiagCalc(M)