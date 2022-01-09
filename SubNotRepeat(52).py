def longestSubWithouRepeat(s):
    maxLen = 0
    curLen = 0
    print(len(s))
    for i in range(len(s)):
        r = i - 1
        while r >= 0 :
            if s[i] == s[r]:
                maxLen = max(maxLen, curLen)
                curLen = 0
                break

            else:
              r -= 1
        curLen += 1
        maxLen = max(maxLen, curLen)

    return maxLen


print(longestSubWithouRepeat(' k a'))