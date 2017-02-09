inputstring=input("give me an input string:\n")
k= {}
for c in inputstring.lower():
    if c in k.keys():
        k[c]+=1
    else:
        k[c]=1
for a,pet in k.items():
    print(a,pet)
