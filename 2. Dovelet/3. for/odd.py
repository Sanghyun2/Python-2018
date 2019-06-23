odd = [] # 홀수들의 list
sum = 0 # 홀수들의 sum
cnt = 7 # 7 inputs

while cnt > 0: # 7 times
    i = input()
    x = int(i)
    if x%2 != 0: # find odd numbers
        odd.append(x)
        sum += x
    cnt -= 1

# print result
if sum != 0:
    print(sum)
    odd.sort()
    print(odd[0])
else:
    print('-1')
