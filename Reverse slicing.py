#x = ["a","b", "c"]
#x.append("D")
#print(x)

def commafy(list):
    #list[-1] = " and "  +   list[-1]
    ''.join(list)
    return' '.join (list)

print (commafy(["trinket", "learning", "fun"]))
print (commafy(["lions", "l", "fun"]))


