
def summation(lst,n):
    sum_lst12 = []
    for i in range(n):
        sum = lst[0][i]+lst[1][i]
        sum_lst12.append(sum)
    return sum_lst12

def min_max(num):
    nummin = min(num)
    nummax = max(num)
    minmax = (nummin, nummax)
    return minmax

n = int(input())
lst = []
for i in range(2):
    lst_num = []
    for j in range(n):
        lst_num.append(int(input()))
    lst.append(lst_num)

num = summation(lst,n)
minmax = min_max(num)

print(num)
print(minmax)
