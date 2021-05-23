import random
def bop(x,y,seed):
    random.seed(seed+x)
    u=random.randint(1,10**8+3)
    random.seed(seed+y)
    v=random.randint(1,10**10+7)
    random.seed(seed)
    x=pow(random.randint(2,2000),u,10**9+7)
    return x^v

def get(s,seed):
    while ')' in s:
        u=s.index(')')
        for t in range(u,-1,-1):
            if s[t]=='(':break
        #print(s,u,t)
        if '#' in s[t:u]:
            v=t+s[t:u].index('#')
            s=s[:t]+str(bop(int(s[t+1:v]),int(s[v+1:u]),seed))+s[u+1:]
        else:
            s=s[:t]+str(eval(s[t+1:u]))+s[u+1:]
    return int(s)

for case in range(1,int(input())+1):
    n=int(input())
    l=[]
    for i in range(n):
        s=input()
        l.append(tuple(get(s,i) for i in range(10)))
    v=[1]
    for i in range(1,n):
        if l[i] in l[:i]:v.append(v[l.index(l[i])])
        else:v.append(max(v)+1)
    z=' '.join(str(i) for i in v)
    print(f'Case #{case}: {z}')
