names= set ()
for x in range (5):
    nm = input ("Enter a name :")
    names.add(nm)
print(names)
nm = input ("Entet a name to modify:")
if nm in names :
    newnm = input ("Enter another name to replace ")
    names.discard(nm)
    names.add(newnm)
else :
    print(nm , "not found in the set")
print(names)
i = 0
while i < 2 :
    nm = input ("Enter the name to delete")
    if nm in names:
        i +=1
        names.discard(nm)
    else :
        print(nm, "Not found in the set.")
print(names)
s.clear()
