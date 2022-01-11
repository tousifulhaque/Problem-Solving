def characterReplacement(s, k):

    char_map = {}
    l = 0
    num_a = 0

    for r in range(len(s)):

        if s[r] in char_map:
            char_map[s[r]] += 1

        else:
            char_map[s[r]] = 1

        while l - r - k +1 not in char_map.values():
