class WayTooLongWords:
  def get(self) :
    x=[]
    n=int(input('How many words do you enter ?\n'))
    if 1<=n<=100:
      while n>0:
        s=input()
        x.append(s)
        n-=1
      for i in x:
        if 1<=len(i)<=100:
          if len(i)<10:
            print(i)
          else:
            a,*b,c=i
            print(a+str(len(b))+c)
        else:
          print(exit(1))
    else:
      print(exit(1))

p=WayTooLongWords()
p.get()

---------------------------------------------------

class WayTooLongWords:
  def get(self) :
    x=[]
    n=int(input('How many words do you enter ?\n'))
    while n>0:
      s=input()
      x.append(s)
      n-=1
    for i in x:
      if len(i)<10:
        print(i)
      else:
        print(i[0]+str(len(i[1:len(i)-1]))+i[len(i)-1])

p=WayTooLongWords()
p.get()

