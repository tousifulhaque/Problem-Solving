def characterReplacement(s, k): #AABABBA

    char_map = {}
    l = 0
    num_a = 0
    max_streak = 0
    for r in range(len(s)): #A
        if s[r] in char_map:
            char_map[s[r]] += 1 #{A:2}

        else:
            char_map[s[r]] = 1 #{A:3, B:2}


        if r-l+1 > k: #2
            while r - l - k +1 > max(list(char_map.values())):  #4-0-1+1
                char_map[s[l]] -=1 #{A:2, B:2}
                l += 1

        max_streak = max(max_streak, r - l + 1) #3
    return max_streak

print(characterReplacement('AABABBA', 1))