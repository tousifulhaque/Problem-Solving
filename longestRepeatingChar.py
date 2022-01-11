def characterReplacement(s, k): #AABABBA

    char_map = {}
    l = 0
    num_a = 0
    max_streak = 0
    for r in range(len(s)):
        print(s[r])
        if s[r] in char_map:
            char_map[s[r]] += 1

        else:
            char_map[s[r]] = 1


        if r-l+1 > k:
            print(char_map.values())
            while r - l - k +1 not in char_map.values():
                char_map[s[l]] -=1
                l += 1

        max_streak = max(max_streak, l - r + 1)
    return max_streak

print(characterReplacement('AABABBA', 1))