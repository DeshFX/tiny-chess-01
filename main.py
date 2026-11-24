import json as j,os,urllib.request as u
U=os.getenv('MAKEFUN_ENV_URL','')
def P(p,b):
 try:return j.load(u.urlopen(U+p,j.dumps(b).encode()))
 except:return 0
SQ=[s for s in range(21,99)if 1<=s%10<=8]
ON=[s in SQ for s in range(120)]
V=[0,100,320,330,500,900,0]
Z=[0,0,5,3,1,2,0]
KN=[-21,-19,-12,-8,8,12,19,21]
DG=[-11,-9,9,11]
ST=[-10,-1,1,10]
KI=DG+ST
OF=[0,0,KN,DG,ST,KI,KI]
CM={21:2,28:1,91:8,98:4,25:3,95:12}
B=[0]*120;T=1;E=0;C=0;K=[25,95];N=0;BD=100000
TT={};KL={};H={}
A=Exception
def k(s,y):
 if B[s-9*y]==y or B[s-11*y]==y:return 1
 for o in KN:
  if B[s+o]==2*y:return 1
 for o in KI:
  if B[s+o]==6*y:return 1
 for d in KI:
  t=s+d
  while ON[t]:
   x=B[t]
   if x:
    if x==5*y or x==(4-(d in DG))*y:return 1
    break
   t+=d
 return 0
def G():
 ms=[]
 for s in SQ:
  x=B[s]
  if x*T<=0:continue
  a=abs(x)
  if a==1:
   d=10*T
   for o,c in ((d,0),(9*T,1),(11*T,1)):
    t=s+o
    if not ON[t]:continue
    y=B[t]
    if (y*T>=0 and t!=E) if c else y:continue
    ms.append((s,t,5 if t//10%7==2 else 0))
    if not c and s//10==3+5*(T<0) and not B[s+2*d]:ms.append((s,s+2*d,0))
  else:
   for d in OF[a]:
    t=s+d
    while ON[t] and not B[t]:
     ms.append((s,t,0))
     if a in(2,6):break
     t+=d
    if ON[t] and B[t]*T<0:ms.append((s,t,0))
 e=K[T<0];q=4**(T<0)
 for d in (2,-2):
  if C&(q<<(d<0)) and not(B[e+d//2]|B[e+d]|B[e-3]*(d<0)) and not(k(e,-T)|k(e+d//2,-T)|k(e+d,-T)):ms.append((e,e+d,0))
 return ms
def M(m):
 global T,E,C
 f,t,p=m;x=B[f];y=B[t];c=t
 if x==T and t==E and not y:c=E-10*T;y=B[c];B[c]=0
 B[t]=x;B[f]=0
 if p:B[t]=p*T
 if abs(x)==6:
  K[T<0]=t
  if abs(t-f)==2:
   r=f-4+7*(t>f);B[f+1-2*(t<f)]=B[r];B[r]=0
 E=(f+t)//2 if x==T and abs(t-f)==20 else 0;C&=~CM.get(f,0)&~CM.get(c,0);T=-T
def v():
 s=0;m=sum(map(V.__getitem__,map(abs,B)))
 for q in SQ:
  x=B[q]
  if not x:continue
  a=abs(x);w=(x>0)*2-1;f=q%10-1;rr=q//10-2 if x>0 else 9-q//10;z=V[a]+(6-abs(f-3)-abs(rr-3))*Z[a]
  if a==1:z+=rr*7
  if a==6:z+=((6-abs(f-3)-abs(rr-3)) if m<2000 else-rr)*12
  s+=z*w
 return s
def O(ms,pl,mv):
 def j(m):
  f,t,p=m;y=B[t]
  if m==mv:return -30000
  z=abs(y) or (B[f]==T and t==E)
  if z:return -(20000+V[z]*10-V[abs(B[f])])
  if p:return -15000
  if m==KL.get(pl):return -12000
  return -H.get((B[f],t),0)//8
 ms.sort(key=j)
def S(d,a,b,pl):
 global N,T,E,BM,C
 N+=1
 if N>BD:raise A
 kc=K[T<0];inch=k(kc,-T)
 if d>0:
  ky=(bytes([x+7 for x in B]),T,C,E)
  e=TT.get(ky)
  if e and e[0]>=d and(e[3]!=2 and e[1]>=b or e[3]==0 or e[3]==2 and e[1]<=a):return e[1]
  mv=e[2] if e else 0
  if d>=3 and not inch and pl>0:
   o=E;E=0;T=-T
   s=-S(d-3,-b,-a,pl+1)
   E=o;T=-T
   if s>=b:return s
  ms=G()
 else:
  if not inch:
   s=v()*T
   if s>=b:return b
   if s>a:a=s
   ms=[m for m in G() if B[m[1]] or m[2] or (B[m[0]]==T and m[1]==E)]
  else:ms=G()
  mv=0
 O(ms,pl,mv);a0=a;best=-1e9;bm=0;cnt=0
 for m in ms:
  f,t,p=m;x=B[f];cap=B[t] or p
  s0=(B[:],T,E,C,K[:])
  M(m);mk=K[T>0]
  if k(mk,T):B[:],T,E,C,K[:]=s0;continue
  cnt+=1
  s=-S(d-1,-b,-a,pl+1)
  B[:],T,E,C,K[:]=s0
  if s>best:best=s;bm=m
  if s>a:a=s
  if a>=b:
   if not cap:KL[pl]=m;H[(x,t)]=H.get((x,t),0)+d*d
   break
 if cnt==0:
  if inch:return -90000+pl
  return 0 if d>0 else a
 if d>0:
  TT[ky]=(d,best,(best>=b)+2*(best<=a0),bm)
  if pl==0:BM=bm
 return best if d>0 else a
def D(u):
 f,t=[ord(u[i])+int(u[i+1])*10-86 for i in(0,2)]
 return (f,t,2+'nbrq'.find(u[4]) if len(u)==5 else 0)
def W(m):
 f,t,p=m
 s='%c%d%c%d'%(f%10+96,f//10-1,t%10+96,t//10-1)
 if p:s+='nbrq'[p-2]
 return s
def R(legal,moves):
 global N,B,T,E,C,BM
 B=[0]*120
 for i,p in enumerate([4,2,3,5,6,3,2,4]):B[21+i]=p;B[31+i]=1;B[81+i]=-1;B[91+i]=-p
 T=1;E=0;C=15;K[0]=25;K[1]=95
 for u in moves:M(D(u))
 ls=set(legal);best=D(legal[0]);N=0;BM=0
 for d in range(1,13):
  try:
   S(d,-1e9,1e9,0)
   if BM and W(BM) in ls:best=BM
  except A:break
 return W(best)
if __name__=='__main__':
 while 1:
  g=P('/game',{})
  if not g or g['status']=='done':break
  while g['status']=='your_move':
   L=g['legal_moves'];n=g['game']
   h=P('/move',{'game':n,'move':R(L,g['moves'])}) or P('/move',{'game':n,'move':L[0]})
   g=h
