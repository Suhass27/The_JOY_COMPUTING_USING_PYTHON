def DiagCalc(li):
   index = len(li)
   rsum =  sum(li[i][i]for i in range(index))
   lsum = sum(li[i][index-i-1]for i in range(index))
   print(rsum)
   print(lsum)
# n = int(input())
# M = []
# for i in range(n):
#     L = list(map(int, input().split()))
#     M.append(L)

# DiagCalc(M)
