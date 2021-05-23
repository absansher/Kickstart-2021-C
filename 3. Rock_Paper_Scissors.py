'''
def score(l,w,e):
    r=p=s=0
    x=w/3+e/3
    for i in range(1,60):
        if l[i-1]=='r':r+=1
        if l[i-1]=='p':p+=1
        if l[i-1]=='s':s+=1
        if l[i]=='r':
            x+=w*p/i+e*s/i
        if l[i]=='p':
            x+=w*s/i+e*r/i
        if l[i]=='s':
            x+=w*r/i+e*p/i
    return x

import random
def jumble():
    return [random.choice(['r','p','s']) for i in range(60)]

v=500
l=jumble()
count=0
best=0
bestp=''
while True:
    count+=1
    curr=score(l,500,v)
    if count%(10**3)==0:
        if curr>best:
            best=curr
            bestp=''.join(l).upper()
            print(best,bestp)
        l=jumble()
    diff=random.randint(0,59)
    change=random.choice(['r','p','s'])
    now=l[diff]
    l[diff]=change
    new=score(l,500,v)
    if new<curr:l[diff]=now
'''
#0:   14233.01145449036  PRRRRRRRRRSSSSSSSSSSSSSSSSSSSSSSSSSSSPPPPPPPPPPPPPPPPPPPPPPP
#50:  14573.497460583536 SPPPPRRRRRRRRRRRRRRRSSSSSSSSSSSSSSSSSSSSSSSSSPPPPPPPPPPPPPPP
#250: 16662.521606975566 SPPRRRRRSSSSSSSSSSPPSPPPPPPPPPPPPPPPPPRRRRRRRRRRRRRRRRRSSSSS
#500: 20810.47947497038  RSPSPRPRSSPRRPSRSPSPPSRRPPSRRSPPSRSSRRPPRRRPSSRPPPSPRSPRSSRS

for case in range(1,int(input())+1):
    if case==1:input()
    x,e=map(int,input().split())
    if e==0      :s='PRRRRRRRRRSSSSSSSSSSSSSSSSSSSSSSSSSSSPPPPPPPPPPPPPPPPPPPPPPP'
    elif e==x//10:s='SPPPPRRRRRRRRRRRRRRRSSSSSSSSSSSSSSSSSSSSSSSSSPPPPPPPPPPPPPPP'
    elif e==x//2 :s='SPPRRRRRSSSSSSSSSSPPSPPPPPPPPPPPPPPPPPRRRRRRRRRRRRRRRRRSSSSS'
    else         :s='RSPSPRPRSSPRRPSRSPSPPSRRPPSRRSPPSRSSRRPPRRRPSSRPPPSPRSPRSSRS'
    print(f'Case #{case}: {s}')
