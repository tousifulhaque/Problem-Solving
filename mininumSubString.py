def minimumSubString(s, t):

    tmap = {}
    smap = {}
    l = 0
    r = 0
    have = 0
    need = 0
    min_len = float('inf')
    min_string = ''
    position_track = []
    for i in t:
        if i in tmap:
            tmap[i] += 1
        else:
            tmap[i] = 1
            need +=1
    # tmap = {a:1 , b: 1, c: 1, d:2}
    # "aaaaaaaaaaaabbbbbcdd"
    while r < len(s): #a1
        if s[r] in tmap :  # B
            if s[r] in smap :
                smap[s[r]] += 1

            else:
                smap[s[r]] = 1 # { a :1}

            if smap[s[r]] == tmap[s[r]]:
                have += 1
        # {a:11 ,b : 5, c : 1, d:2 }
        while have == need  :
                if (s[l] in tmap) :
                    if r - l +1 < min_len:
                        min_len = r - l + 1  # 2
                        min_string = s[l:(r + 1)] #ab
                    smap[s[l]] -=1
                    if smap[s[l]] < tmap[s[l]]:
                        print(smap)
                        have -=1
                l += 1

        r += 1
    return min_string


s =  "aaaaaaaaaaaabbbbbcdd"
t = "abcdd"

print(minimumSubString(s, t))
