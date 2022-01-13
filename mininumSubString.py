def minimumSubString(s, t):
    tmap = {}
    smap = {}
    l = 0
    r = 0
    min_string = s
    for i in t:
        if i in tmap:
            tmap[i] += 1
        else:
            tmap[i] = 1

    while r < len(s):
        if s[r] in tmap: #A
            if s[r] in smap:
                smap[s[r]] += 1 #{A: 1, B:1, C:1  }
            else:
                smap[s[r]] = 1

            while smap == tmap :
                if r-l+1 < len(min_string) :
                    min_string = s[l:r+1]
                smap[s[l]] -= 1
                l -= 1
        r += 1
    return min_string

s = "ADOBECODEBANC"
t = "ABC"

print(minimumSubString(s,t))
