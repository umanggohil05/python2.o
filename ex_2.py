import random
x = {random.randint(15,45) for i in range (10)}
s1 = set ()
c  =0
for i in x :
    if i <30:
        c = c +1
for i in x :
    if i <36:
        s1.add(i)
print(x,c,s1)

