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

    while r < len(s):
        if s[r] in tmap:  # B
            if s[r] in smap :
                smap[s[r]] += 1
                if smap[s[r]] > tmap[s[r]] :
                    l = r
                    smap = {s[r]: 1}
            else:
                smap[s[r]] = 1
            position_track.append(r)  # [0, 3, 5]
            if smap == tmap:
                if r - l + 1 < min_len:
                    min_len = r - l + 1  # 5
                    min_string = s[l:r + 1]
                smap[s[l]] -= 1
                l = position_track.pop(0)  # 3
        r += 1
    return min_string


s = "ab"
t = "b"

print(minimumSubString(s, t))
