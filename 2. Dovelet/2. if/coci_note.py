s1, s2, s3, s4, s5, s6, s7, s8 = input().split()

a = [int(s1), int(s2), int(s3), int(s4), int(s5), int(s6), int(s7), int(s8)]

if a[0] > a[1] :
    if a[1] > a[2] :
        if a[2] > a[3] :
            if a[3] > a[4] :
                if a[4] > a[5] :
                    if a[5] > a[6] :
                        if a[6] > a[7] :
                            print("descending")
                        else :
                            print("mixed")
                    else :
                        print("mixed")
                else:
                    print("mixed")
            else:
                print("mixed")
        else:
            print("mixed")
    else:
        print("mixed")
elif a[7] > a[6] :
    if a[6] > a[5] :
        if a[5] > a[4] :
            if a[4] > a[3] :
                if a[3] > a[2] :
                    if a[2] > a[1] :
                        if a[1] > a[0] :
                            print("ascending")
                        else :
                            print("mixed")
                    else:
                        print("mixed")
                else:
                    print("mixed")
            else:
                print("mixed")
        else:
            print("mixed")
    else:
        print("mixed")
else : print("mixed")
