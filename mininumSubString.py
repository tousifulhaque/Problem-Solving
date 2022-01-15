def minimumSubString(s, t):

    tmap = {}
    smap = {}
    l = 0
    r = 0
    min_len = float('inf')
    min_string = ''
    position_track = []
    for i in t:
        if i in tmap:
            tmap[i] += 1
        else:
            tmap[i] = 1
    # "ADOBECODEBANC"
    while r < len(s): #2
        if s[r] in tmap:  # B
            if s[r] in smap :
                smap[s[r]] += 1
                if smap[s[r]] > tmap[s[r]] :
                    l = r
                    smap = {s[r]: 1}
            else:
                smap[s[r]] = 1 # { a :1 , b :1}

            while smap == tmap :
                if (s[l] in t and (smap[s[l]] != 0)) :
                    if r -l +1 < min_len:
                        min_len = r - l + 1  # 2
                        min_string = s[l:r + 1] #ab
                    smap[s[l]] -=1
                l += 1

        r += 1
    return min_string


s =  "ADOBECODEBANC"
t =  'ABC'

print(minimumSubString(s, t))
