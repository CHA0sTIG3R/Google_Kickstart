def checkbor(inp):
    strinp= str(inp)
    
    res = []
    for i in strinp:
        if int(i)%2 == 1:
            res.append(1)
        else:
            res.append(0)
    
    if res[0] == 1:
        bore = True
        i = 1
        while i < len(res):
            if res[i] == res[i-1]:
                bore = False
                break
            else:
                bore = True
            i+=1
    else:
        bore = False
    return bore
def boringNum(l,r):
    numlst = [i for i in range(l, r+1)]
    borlst = []
    for i in numlst:
        if checkbor(i):
            borlst.append(i)
    return len(borlst)

t = int(input())
for i in range(1, t+1):
    l,s = [int(j) for j in input().split()]
    print(f"Case #{i}: {boringNum(l,s)}")