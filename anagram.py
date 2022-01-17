def anagram(s, t):
    tmap = {}
    smap = {}
    for i in s:
        smap[i] = 1 + smap.get(i,0)
    for i in t:
        tmap[i] = 1+ tmap.get(i, 0)
    print(tmap)
    print(smap)
    return tmap == smap

s = "rat"
t = "cat"
print(anagram(s,t))