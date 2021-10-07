a=[]
n=int(input('Dati dimensiunile matricii: '))
if n>=2 and n<=10 :
    for i in range(0,n):
        v=[]
        for j in range(0,n):
            x=int(input('Dati numarul: '))
            v.append(x)
        a.append(v)
    print(a)

"""diagonala principala"""
dp=[]
for x in range(len(a)):
    for y in range(len(a[0])):
        if x==y:
            dp.append(a[x][y])
print('suma diagonala principala: ', sum(dp))

"""diagonala secundara"""
ds=[]
for x in range(len(a)):
    for y in range(len(a[0])):
        if x+y==n-1:
            ds.append(a[x][y])
print('suma diagonala secundara: ', sum(ds))

"""diagonala principala sus"""
dp1=[]
for x in range(len(a)):
    for y in range(len(a[0])):
        if x<y:
            dp1.append(a[x][y])
print('suma elementelor de mai sus de diagonala principala: ', sum(dp1))

"""diagonala principala jos"""
dp2=[]
for x in range(len(a)):
    for y in range(len(a[0])):
        if (x+y)>(n-1):
            dp2.append(a[x][y])
print('suma elementelor de mai jos de diagonala principala: ', sum(dp2))

"""diagonala secundara sus"""
dp3=[]
for x in range(len(a)):
    for y in range(len(a[0])):
        if (x+y)<(n-1):
            dp3.append(a[x][y])
print('suma elementelor de mai sus de diagonala secundara:', sum(dp3))

"""diagonala secundara jos"""
dp4=[]
for x in range(len(a)):
    for y in range(len(a[0])):
        if (x+y)>(n-1):
            dp4.append(a[x][y])
print('suma elementelor de mai sus de diagonala secundara:', sum(dp4))