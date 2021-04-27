alp="abcdefghigklmnopqrstuvwxyz"

st=input("Input binary numbers: ")

n=0

for i in range(len(st)) :
  if st[i]=='1':
    print(alp[n] , end=' ')
    n=0

  else:
    n+=1

# 1 -->  0 --> n=1
# 2 -->  1 --> n=1  > b
# 3 -->  0 --> n=2
# 4 -->  0 --> n=3
# 5 -->  1 --> n=3  > c
