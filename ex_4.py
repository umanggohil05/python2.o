s1 = {'aagam', 'bindu' , 'anshul','aaryan', 'ashit' , "brijesh"}
s2 = set()
s3 = set()
for x in s1:
    if x[0] == 'A' or x[0] == 'a':
        s2.add(x)
    elif x[0] == 'B' or x[0] == 'b':
        s3.add(x)

print("values beginning with A:",s2)
print("alues beginning with B:",s3)
