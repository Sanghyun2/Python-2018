# verify Triangle

s1, s2, s3 = input().split()

in1 = int(s1)
in2 = int(s2)
in3 = int(s3)

list = [in1,in2,in3]

max = 0
min = 0

for i in range(0,3): # find maximum value
  if list[i] > max:
    max = list[i]

list.remove(max) # remove maximum value from list

sum = list[0]+list[1]

if sum > max: # print answer
  print('yes')
else:
  print('no')
