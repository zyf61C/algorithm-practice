def height(l):
    s = 0
    for k in range(max(l)):
        for i in range(1,len(l)-1):
            l[i]+=1
            s+=1
            f = 0
            t = 0
            for j in range(i+1,len(l)):
                if l[i]<=l[j]:
                    f = 1
                    break
                    #print("f = 1")

            for j in range(i-1,-1,-1):
                if l[i]<=l[j]:
                    #print()
                    t = 1

            if f == 0 or t == 0:
                #print('del',l)
                l[i]-=1
                s-=1
        print(l)
    return s
print(height([3, 0, 0, 2, 0, 4]))