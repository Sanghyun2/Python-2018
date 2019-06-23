a = int(input()) # receive the input
b = 1
while b <= a : # repeat n times
    if b == 1 or b == a or b == int(a/2) + 1 : # 3 cases for printing the '*' n times
        print("*" * a)
    else : print("*") # else cases
    b = b + 1
