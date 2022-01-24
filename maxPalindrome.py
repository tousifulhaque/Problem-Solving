def longestPalindrome(s):
    l = 0
    r = 1 
    maxLen = 0
    maxPalindrome = ""
    if len(s) == 1:
        return s

    while r < len(s):
        while l <= r: #l = 0  r = 3 
            if s[l].lower() == s[r].lower(): #ba
                if s[l : r+1] == s[l : r+1][::-1]:
                    if r-l+1 > maxLen:
                        maxPalindrome = s[l : r+1] #bab
                        maxLen = r-l+1 
            l += 1
        l = 0
        r += 1 # l = 2
    
    return maxPalindrome

s = "ac"
print(longestPalindrome(s))